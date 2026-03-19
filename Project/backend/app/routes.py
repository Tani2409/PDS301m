from flask import Blueprint, jsonify
from app.services.silver_service import get_7_days_silver_price
from app.services.scraper_service import scrape_silver_price

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/silver-price', methods=['GET'])
def get_silver_price():
    try:
        data = get_7_days_silver_price()
        return jsonify({
            "status": "success",
            "data": data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@api_bp.route('/api/live-silver-price', methods=['GET'])
def get_live_silver_price():
    try:
        live_price = scrape_silver_price()
        if live_price is not None:
             return jsonify({
                 "status": "success",
                 "price": live_price
             })
        else:
             return jsonify({
                 "status": "error",
                 "message": "Không thể lấy giá live"
             }), 500
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
