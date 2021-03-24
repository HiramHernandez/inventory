from sqlalchemy import exc, func
from  .extensions import db
from .models import (
    Store,
    Product,
    InitialInventory,
    DetailInitialInventory,
    PhysicalInventory,
    DetailPhysicalInventory
)


class StoreService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def create(self, **kwargs):
        new_store = Store(**kwargs)
        try:
            db.session.add(new_store)
            db.session.commit()
            return (True, new_store.to_dict())
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return (False, None)

    def fetch(self):
        try:
            stores = Store.query.all()
            return [
                {
                    "id_rienda": store.id_tienda,
                    "nombre": store.nombre,
                    "direccion": store.direccion
                } for store in stores
            ]
        except exc.SQLAlchemyError as e:
            print('Ha ocurrido un error')
            return None
       


class ProductService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def create(self, **kwargs):
        new_product = Product(**kwargs)
        try:
            db.session.add(new_product)
            db.session.commit()
            return (True, new_product.to_dict())
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return (False, None)

    def fetch(self):
        products = Product.query.all()
        return [
            {
                'id_producto': product.id_producto,
                'nombre': product.nombre,
                'sku': product.sku,
                'precio': product.precio
            } for product in products
        ]


class InitialInventoryService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def create(self, **kwargs):
        new_inventory = InitialInventory(**kwargs)
        try:
            db.session.add(new_inventory)
            db.session.commit()
            return (True, new_inventory.to_dict())
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return (False, None)
        pass

    def create_detail(self, **kwargs):
        new_inventory = DetailInitialInventory(**kwargs)
        try:
            db.session.add(new_inventory)
            db.session.commit()
            return (True, new_inventory.to_dict())
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return (False, None)

    def fetch(self):
        inventories = InitialInventory.query.all()
        return [
            {
                'id_inventario_inicial': inventory.inventario_inicial,
                'fecha': inventory.fecha
            } for inventory in inventories
        ]
        

    def fetch_detail(self):
        inventories_detail = DetailInitialInventory.query.all()
        return [
            {
                'id_inventario_inicial_detalle': inventory.id_inventario_inicial_detalle,
                'id_inventario_inicial': inventory.id_inventario_inicial,
                'cantidad': inventoy.cantidad,
                'id_producto': inventory.id_producto
            } for inventory in inventories_detail
        ]


class PhysicalInventoryService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def create(self, **kwargs):
        new_inventory = PhysicalInventory(**kwargs)
        try:
            db.session.add(new_inventory)
            db.session.commit()
            return (True, new_inventory.to_dict())
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return (False, None)


    def create_detail(self, **kwargs):
        new_inventory = DetailPhysicalInventory(**kwargs)
        try:
            db.session.add(new_inventory)
            db.session.commit()
            return (True, new_inventory.to_dict())
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return (False, None)

    def fetch(self):
        inventories = PhysicalInventory.query.all()
        return [inventory.to_dict() for inventory in inventories]

    def fetch_detail(self, pk):
        inventories = DetailPhysicalInventory \
            .query \
            .filter(DetailPhysicalInventory.id_inventario_fisico == pk) \
            .all()
        return [inventory.to_dict() for inventory in inventories]

    def check_stock(self, pk_store, pk_product, date):
        initial_iventory = db.session \
            .query(
                func.coalesce(
                    func.sum(DetailInitialInventory.cantidad), 0
                )
            ) \
            .filter(DetailInitialInventory.id_producto == pk_product) \
            .group_by(DetailInitialInventory.id_producto) \
            .scalar()
        pyhsical_inventory = db.session \
            .query(
                func.coalesce(
                    func.sum(DetailPhysicalInventory.cantidad)    
                ,0)
            ) \
            .select_from(DetailPhysicalInventory) \
            .join(
                PhysicalInventory,
                PhysicalInventory.id_inventario_fisico == DetailPhysicalInventory.id_inventario_fisico
            ) \
            .filter(
                PhysicalInventory.id_tienda == pk_store,
                DetailPhysicalInventory.id_producto == pk_product,
                PhysicalInventory.fecha <= date
            ) \
            .group_by(DetailPhysicalInventory.id_producto) \
            .scalar()
        value_initial = initial_iventory if initial_iventory else 0
        value_physical = pyhsical_inventory if pyhsical_inventory else 0
        return value_initial + value_physical
