from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

engine = create_engine("sqlite:///database.db")
Base = declarative_base()

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    price = Column(Integer)
    orders = relationship("Order", backref = "product")

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String)
    orders = relationship("Order", backref = "customer")

class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key = True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer)
    order_date = Column(DateTime, default = datetime.now)

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()