from flask import Blueprint, jsonify, request
from app.services.silver_service import SilverService

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/silver-price', methods=['GET'])
def get_silver_price():
    """
    Lấy giá bạc trực tuyến hiện tại (Live)
    ---
    tags:
      - Silver Data
    responses:
      200:
        description: Thông tin giá bạc spot, USD/VND và giá quy đổi nội địa
    """
    try:
        data = SilverService.get_live_data()
        return jsonify({"status": "success", "live": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/silver-history', methods=['GET'])
def get_silver_history():
    """
    Lấy dữ liệu lịch sử giá bạc từ Dataset
    ---
    tags:
      - Silver Data
    responses:
      200:
        description: Danh sách giá bạc lịch sử
    """
    try:
        data = SilverService.get_historical_data()
        if data is None:
            return jsonify({"status": "error", "message": "Dataset not found"}), 404
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/silver-weekly', methods=['GET'])
def get_silver_weekly():
    """
    Lấy dữ liệu giá bạc trong 7 ngày gần nhất
    ---
    tags:
      - Silver Data
    responses:
      200:
        description: Danh sách giá bạc theo ngày
    """
    try:
        data = SilverService.get_weekly_price()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/calculate/conversion', methods=['POST'])
def calculate_conversion():
    """
    Quy đổi giá trị bạc dựa trên khối lượng và đơn vị
    ---
    tags:
      - Calculators
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            live_price:
              type: number
            amount:
              type: number
            unit:
              type: string
              enum: [chi, tael, oz]
            purity:
              type: number
    responses:
      200:
        description: Kết quả quy đổi sang VND và USD
    """
    try:
        data = request.get_json(silent=True) or {}
        res = SilverService.calculate_conversion(
            data.get('live_price', data.get('spot', 32.5)),
            data.get('usd_vnd', data.get('usdvnd', 25000.0)),
            data.get('amount', data.get('quantity', 1)),
            data.get('unit', 'chi'),
            data.get('purity', 1.0)
        )
        return jsonify({"status": "success", "result": res})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/calculate/risk', methods=['POST'])
def calculate_risk():
    """
    Tính toán rủi ro chênh lệch (Spread Risk)
    ---
    tags:
      - Calculators
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
             bid:
               type: number
               example: 1180000
             ask:
               type: number
               example: 1220000
    responses:
      200:
        description: Kết quả phân tích rủi ro
    """
    try:
        data = request.get_json(silent=True) or {}
        bid = data.get('bid', data.get('buyPrice', 0))
        ask = data.get('ask', data.get('sellPrice', 0))
        res = SilverService.calculate_risk(bid, ask)
        return jsonify({"status": "success", "result": res})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/calculate/investment', methods=['POST'])
def calculate_investment():
    """
    So sánh lợi nhuận đầu tư bạc với gửi tiết kiệm ngân hàng
    ---
    tags:
      - Calculators
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            capital:
              type: number
            rate_annual:
              type: number
            months:
              type: integer
            silver_profit:
              type: number
    responses:
      200:
        description: So sánh lợi nhuận giữa hai hình thức
    """
    try:
        data = request.get_json(silent=True) or {}
        res = SilverService.compare_investment(
            data.get('capital', data.get('initial', 0)),
            data.get('rate_annual', data.get('rate', 0)),
            data.get('months', 3),
            data.get('silver_profit', data.get('final', 0) - data.get('initial', 1))
        )
        return jsonify({"status": "success", "result": res})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/calculate/portfolio', methods=['POST'])
def calculate_portfolio():
    """
    Tính toán tổng lợi nhuận danh mục đầu tư (Bài tập 3)
    ---
    tags:
      - Calculators
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            transactions:
              type: array
              items:
                type: object
                properties:
                  buy_price:
                    type: number
                  sell_price:
                    type: number
                  quantity:
                    type: number
    responses:
      200:
        description: Tổng vốn, tổng lãi/lỗ và ROI
    """
    try:
        data = request.get_json(silent=True) or {}
        res = SilverService.calculate_portfolio(data.get('transactions', []))
        return jsonify({"status": "success", "result": res})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/calculate/breakeven', methods=['POST'])
def calculate_breakeven():
    """
    Tính toán giá bạc cần thiết để hòa vốn so với gửi ngân hàng
    ---
    tags:
      - Calculators
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            purchase_price:
              type: number
            bank_rate:
              type: number
            months:
              type: integer
    responses:
      200:
        description: Giá hòa vốn mục tiêu
    """
    try:
        data = request.get_json(silent=True) or {}
        res = SilverService.calculate_breakeven(
            data.get('purchase_price', data.get('buyPrice', 0)),
            data.get('bank_rate', data.get('bankRate', 0)),
            data.get('months', 3)
        )
        return jsonify({"status": "success", "result": res})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/market/histogram', methods=['GET'])
def get_histogram():
    """
    Lấy dữ liệu phân phối giá bạc (Histogram)
    ---
    tags:
      - Market
    responses:
      200:
        description: Dữ liệu phân bổ theo khoảng giá
    """
    try:
        data = SilverService.get_histogram_data()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/market/branded', methods=['GET', 'POST'])
def get_branded():
    """
    Lấy giá bạc theo các thương hiệu niêm yết (SJC, DOJI, PNJ)
    ---
    tags:
      - Market
    parameters:
      - name: body
        in: body
        required: false
        schema:
          type: object
          properties:
            basePrice:
              type: number
    responses:
      200:
        description: Danh sách giá theo thương hiệu
    """
    try:
        # Sử dụng get_json(silent=True) cho phép xử lý cả GET (không có body) và POST (có body)
        data = request.get_json(silent=True) or {}
        base = data.get('basePrice', 0)
        res = SilverService.get_branded_prices(base)
        return jsonify({"status": "success", "data": res})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/market/insights', methods=['GET'])
def get_insights():
    """
    Lấy các thông tin thị trưởng và phân tích chuyên sâu
    ---
    tags:
      - Market
    responses:
      200:
        description: Thông tin ngày lễ, tỷ lệ quy đổi và đỉnh lịch sử
    """
    try:
        data = SilverService.get_market_insights()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
