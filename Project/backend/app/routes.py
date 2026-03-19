from flask import jsonify
from .services.silver_service import SilverService

def register_routes(app):
    @app.route('/api/silver-price', methods=['GET'])
    def get_silver_price():
        """Lấy giá 7 ngày qua và giá Live."""
        try:
            weekly = SilverService.get_weekly_price()
            live = SilverService.get_live_data()
            return jsonify({
                "status": "success",
                "data": weekly,
                "live": live
            })
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    @app.route('/api/silver-history', methods=['GET'])
    def get_silver_history():
        """Lấy dữ liệu CSV dài hạn cho biểu đồ."""
        try:
            data = SilverService.get_historical_data()
            if data is None:
                return jsonify({"status": "error", "message": "CSV data not found"}), 404
            return jsonify({"status": "success", "data": data})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
