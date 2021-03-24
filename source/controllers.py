from flask import request
from flask_restful import Resource
from .services import (
    StoreService,
    ProductService,
    InitialInventoryService,
    PhysicalInventoryService
)


class StoreListController(Resource):

    def __init__(self):
        self.store_service = StoreService()

    def post(self):
        payload = request.get_json(force=True)
        payload = {
            key: value for (key, value) in payload.items() \
                if value is not None
        }
        create = self.store_service.create(**payload)
        return ({'data': create[1], 'message': 'success'}, 201) if create[0] else \
            ({'data': None, 'message': 'Ocurrio un error'}, 400)

    def get(self):
        data = self.store_service.fetch()
        return ({'data': data}, 200) if data else ({'data': None}, 404)


class ProductListController(Resource):
    def __init__(self):
        self.product_service = ProductService()

    def post(self):
        payload = request.get_json(force=True)
        payload = {
            key: value for (key, value) in payload.items() \
                if value is not None
        }
        create = self.product_service.create(**payload)
        return ({'data': create[1], 'message': 'success'}, 201) if create[0] else \
            ({'data': None, 'message': 'Ocurrio un error'}, 400)

    def get(self):
        data = self.product_service.fetch()
        return ({'data': data}, 200) if data else ({'data': None}, 404)


class PhysicalInventoryListController(Resource):
    def __init__(self):
        self.physicall_iventory_service = PhysicalInventoryService()

    def post(self):
        payload = request.get_json(force=True)
        payload = {
            key: value for (key, value) in payload.items() \
                if value is not None
        }
        create = self.physicall_iventory_service.create(**payload)
        return ({'data': create[1], 'message': 'success'}, 201) if create[0] else \
            ({'data': None, 'message': 'Ocurrio un error'}, 400)

    def get(self):
        data = self.physicall_iventory_service.fetch()
        return ({'data': data}, 200) if data else ({'data': None}, 404)

class DetailPhysicalInventoryListController(Resource):

    def __init__(self):
        self.physicall_iventory_service = PhysicalInventoryService()

    def post(self, pk):
        payload = request.get_json(force=True)
        payload = {
            key: value for (key, value) in payload.items() \
                if value is not None
        }
        payload['id_inventario_fisico'] = pk
        create = self.physicall_iventory_service.create_detail(**payload)
        return ({'data': create[1], 'message': 'success'}, 201) if create[0] else \
            ({'data': None, 'message': 'Ocurrio un error'}, 400)

    def get(self, pk):
        data = self.physicall_iventory_service.fetch_detail(pk)
        self.physicall_iventory_service.check_stock(4, 1, '2021-03-21')
        return ({'data': data}, 200) if data else ({'data': None}, 404)


class CheckStockProductController(Resource):

    def __init__(self):
        self.physicall_iventory_service = PhysicalInventoryService()

    def get(self, pk_store, pk_product, amount, date):
        stock = self.physicall_iventory_service.check_stock(pk_store, pk_product, date)
        if stock < amount:
            return {'data': None, 'message': 'No hay suficiente producto en la tienda'}, 400
        return {
            'data': {
                'stock': stock,
                'amount': amount
            }
        }, 200

