import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Init App

# Init db
db = SQLAlchemy()

# Init marshamallow
ma = Marshmallow()

# # Product Class/Model
class Product(db.Model):
    __tablename__ = 'Products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name =  name
        self.description = description
        self.price = price
        self.qty = qty


    def save(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()
        

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

# Product Schema
class ProductSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'name', 'description', 'price', 'qty')

# Init Schema
# No need to use strict as Marsh 3.xx is always strict
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

