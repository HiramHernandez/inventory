from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    Float,
    Date
)
from .extensions import db

class Store(db.Model):
    __tablename__ = 'tienda'
    id_tienda = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(VARCHAR(length=50), nullable=False)
    direccion = Column(VARCHAR(length=100))

    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def __repr__(self):
        return f"<Store {self.nombre}>"

    def to_dict(self):
        return {
            'id_tienda': self.id_tienda,
            'nombre': self.nombre,
            'direccion': self.direccion
        }


class Product(db.Model):
    __tablename__ = 'productos'
    id_producto = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(VARCHAR(length=50), nullable=False)
    sku = Column(VARCHAR(length=50), nullable=False)
    precio = Column(Float, nullable=False)

    def __init__(self, nombre, sku, precio):
        self.nombre = nombre
        self.sku = sku
        self.precio = precio

    def to_dict(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'sku': self.sku,
            'precio': self.precio
        }


class InitialInventory(db.Model):
    __tablename__ = 'inventario_inicial'
    id_inventario_inicial = Column(Integer, primary_key=True, nullable=False)
    fecha = Column(Date)

    def __init__(self, fecha):
        self.fecha = fecha

    def to_dict(self):
        return {
            'id_inventario_inicial': self.id_inventario_inicial,
            'fecha': str(self.fecha)
        }


class DetailInitialInventory(db.Model):
    __tablename__ = 'inventario_inicial_detalle'
    id_inventario_inicial_detalle = Column(Integer, primary_key=True, nullable=False)
    id_inventario_inicial = Column(Integer)
    cantidad = Column(Integer)
    id_producto = Column(Integer)

    def __init__(self, id_inventario_inicial, cantidad, id_producto):
        self.id_inventario_inicial = id_inventario_inicial
        self.cantidad = cantidad
        self.id_producto = id_producto


class PhysicalInventory(db.Model):
    __tablename__ = 'invetario_fisico'
    id_inventario_fisico = Column(Integer, primary_key=True, nullable=False)
    fecha = Column(Date)
    id_tienda = Column(Integer)

    def __init__(self, fecha, id_tienda):
        self.fecha = fecha
        self.id_tienda = id_tienda

    def to_dict(self):
        return {
            'id_inventario_fisico': self.id_inventario_fisico,
            'fecha': str(self.fecha),
            'id_tienda': self.id_tienda
        }


class DetailPhysicalInventory(db.Model):
    __tablename__ = 'id_inventario_fisico_detalle'
    id_inventario_fisico_detalle = Column(Integer, primary_key=True, nullable=False)
    id_inventario_fisico = Column(Integer)
    id_producto = Column(Integer)
    cantidad = Column(Integer)
    motivo = Column(VARCHAR(length=50))

    def __init__(self, id_inventario_fisico, id_producto , cantidad, motivo):
        self.id_inventario_fisico = id_inventario_fisico
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.motivo = motivo

    def to_dict(self):
        return {
            'id_inventario_fisico_detalle': self.id_inventario_fisico_detalle,
            'id_inventario_fisico': self.id_inventario_fisico,
            'id_producto': self.id_producto,
            'cantidad': self.cantidad,
            'motivo': self.motivo
        }
