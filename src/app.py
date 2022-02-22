import os
from flask import Flask
from . import models, api, views


basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    
    # Database 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        models.db.init_app(app)




    # Blueprints
    app.register_blueprint(api.product.bp, url_prefix='/')
    app.register_blueprint(views.setup.bp, url_prefix='/setup')


    return app 
