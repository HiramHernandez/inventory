import os
from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    Column,
    Integer,
    VARCHAR
)
from gevent import monkey
from .extensions import db
from .controllers import (
    StoreListController,
    ProductListController,
    PhysicalInventoryListController,
    DetailPhysicalInventoryListController,
    CheckStockProductController
)

monkey.patch_all()
app = Flask(__name__)

app.config.from_json(os.path.abspath(os.path.join('settings.json')))
db.init_app(app)

resourses = Blueprint('url_global', __name__)
api = Api(resourses, prefix='/api/')
api.add_resource(StoreListController, 'stores')
api.add_resource(ProductListController, 'products')
api.add_resource(PhysicalInventoryListController, 'physicall-inventory')
api.add_resource(DetailPhysicalInventoryListController, 'physicall-inventory/<int:pk>/detail')
api.add_resource(CheckStockProductController, 'stoker/<int:pk_store>/product/<int:pk_product>/amount/<int:amount>/date/<date>/stock')

app.register_blueprint(resourses)
