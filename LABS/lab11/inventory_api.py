# inventory_api.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store for products
products = [
    {
        'id': 101,
        'name': 'Laptop',
        'price': 1200.00,
        'stock': 50
    },
    {
        'id': 102,
        'name': 'Wireless Mouse',
        'price': 25.50,
        'stock': 150
    },
    {
        'id': 103,
        'name': 'Mechanical Keyboard',
        'price': 75.00,
        'stock': 80
    }
]
next_product_id = 104

# [READ] Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({'products': products})

# [READ] Get a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'product': product})

# [CREATE] Add a new product
@app.route('/products', methods=['POST'])
def create_product():
    if not request.json or not all(k in request.json for k in ['name', 'price', 'stock']):
        return jsonify({'error': 'Bad Request: Missing name, price, or stock'}), 400
    
    global next_product_id
    new_product = {
        'id': next_product_id,
        'name': request.json['name'],
        'price': float(request.json['price']),
        'stock': int(request.json['stock'])
    }
    products.append(new_product)
    next_product_id += 1
    return jsonify({'product': new_product}), 201

# [UPDATE] Update product details
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    if not request.json:
        return jsonify({'error': 'Bad Request: Invalid JSON'}), 400

    product['name'] = request.json.get('name', product['name'])
    product['price'] = float(request.json.get('price', product['price']))
    product['stock'] = int(request.json.get('stock', product['stock']))
    return jsonify({'product': product})

# [CUSTOM ACTION] Sell a quantity of a product
@app.route('/products/<int:product_id>/sell', methods=['POST'])
def sell_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    
    if not request.json or 'quantity' not in request.json:
        return jsonify({'error': 'Bad Request: Missing quantity'}), 400
    
    quantity_to_sell = int(request.json['quantity'])
    
    if product['stock'] < quantity_to_sell:
        return jsonify({
            'error': 'Insufficient stock',
            'stock_available': product['stock']
        }), 400 # Bad Request because the client asked for too many
        
    product['stock'] -= quantity_to_sell
    return jsonify({
        'message': 'Sale successful',
        'product': product
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
