from distutils.log import error
from flask import Blueprint, jsonify, request, json, Response
from .. import models


bp = Blueprint('product', __name__)


# Get all products
@bp.route('/product', methods=['GET'])
def get_products():
    all_products = models.Product.query.all()
    result = models.products_schema.dump(all_products)
    return jsonify(result), 200

    

# Get Single products
@bp.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = models.Product.query.get(id)
    return models.product_schema.jsonify(product), 200

# Create a Product 
@bp.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    new_product = models.Product(name, description, price, qty)
    new_product.save()
    return 'OK', 200


# Update Product
@bp.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    request_data = request.get_json()
    product = models.Product.query.get(id)
    product.update(request_data)
    return models.product_schema.jsonify(product), 200



# Delete products
@bp.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = models.Product.query.get(id)
    product.delete()
    return models.product_schema.jsonify(product), 200


# def custom_response(res, status_code):
#   """
#   Custom Response Function
#   """
#   return Response(
#     mimetype="application/json",
#     response=json.dumps(res),
#     status=status_code
#   )