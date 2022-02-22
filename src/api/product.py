from flask import Blueprint, jsonify, request
from .. import models


bp = Blueprint('product', __name__)


# Get all products
@bp.route('/product', methods=['GET'])
def get_products():
    all_products = models.Product.query.all()
    result = models.products_schema.dump(all_products)
    return jsonify(result)

    

# Get Single products
@bp.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = models.Product.query.get(id)
    return models.product_schema.jsonify(product)



# Create a Product 
@bp.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = models.Product(name, description, price, qty)
    new_product.save()


    return models.product_schema.jsonify(new_product)

# Update a Product 
@bp.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    product = models.Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    models.db.session.commit()
    
    return models.product_schema.jsonify(product)


# Delete products
@bp.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = models.Product.query.get(id)
    product.delete()
    return models.product_schema.jsonify(product)


