from flask import Blueprint, jsonify, request
from app.services.silver_service import SilverService

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/silver-price', methods=['GET'])
def get_silver_price():
    try:
        data = SilverService.get_live_data()
        return jsonify({"status": "success", "live": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/silver-history', methods=['GET'])
def get_silver_history():
    try:
        data = SilverService.get_historical_data()
        if data is None:
            return jsonify({"status": "error", "message": "Dataset not found"}), 404
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/silver-weekly', methods=['GET'])
def get_silver_weekly():
    try:
        data = SilverService.get_weekly_price()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/calculate/conversion', methods=['POST'])
def calculate_conversion():
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
    try:
        data = request.get_json(silent=True) or {}
        res = SilverService.calculate_portfolio(data.get('transactions', []))
        return jsonify({"status": "success", "result": res})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/calculate/breakeven', methods=['POST'])
def calculate_breakeven():
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
    try:
        data = SilverService.get_histogram_data()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/api/market/branded', methods=['GET', 'POST'])
def get_branded():
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
    try:
        data = SilverService.get_market_insights()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
