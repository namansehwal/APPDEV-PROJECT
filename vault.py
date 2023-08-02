from sqlalchemy import create_engine, Column, Integer, String, update, delete
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import time

engine = create_engine('sqlite:///database.sqlite3', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
agent = Session()



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name',String)
    email = Column('email',String)
    password = Column('password', String)
    address = Column('address', String)
    phone_number = Column('phone_number', String)
    admin = Column('admin', Integer, default=0)
    
    def __init__(self, name, email,password, address, phone_number):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.phone_number = phone_number
  


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name',String)
    image = Column('image',String)
    date = Column('date',String)
    
    def __init__(self, name, image, date):
        self.name = name
        self.image = image
        self.date = date

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name',String)
    category = Column('category',String)
    category_id = Column('category_id', Integer, foreign_key='categories.id')
    price = Column('price', Integer)
    quantity = Column('quantity', Integer)
    time = Column('time', Integer)
    image = Column('image', String)
    description = Column('description', String)
    si_unit = Column('si_unit', Integer)
    
    def __init__(self, name, category, category_id, price, quantity, time, image, description, si_unit):
        self.name = name
        self.category = category
        self.category_id = category_id
        self.price = price
        self.quantity = quantity
        self.time = time
        self.image = image
        self.description = description
        self.si_unit = si_unit

class Cart(Base):
    __tablename__ = 'cart'
    cart_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer)
    product_id = Column('product_id', Integer)
    product_name = Column('product_name', String)
    quantity = Column('quantity', Integer)
    price = Column('price', Integer)
    created_at = Column('created_at', String)
    
    def __init__(self, user_id, product_id, product_name, quantity, price):
        self.user_id = user_id
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.created_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())




class Order_Items(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer)
    order_id = Column('order_id', Integer)
    product_id = Column('product_id', Integer)
    quantity = Column('quantity', Integer)
    amount = Column('amount', Integer)
    created_at = Column('created_at', String)
    
    def __init__(self, user_id, order_id, product_id, quantity, amount):
        self.user_id = user_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.amount = amount
        self.created_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class Order_Detail(Base):
    __tablename__ = 'order_detail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer)
    total = Column('total', Integer)
    created_at = Column('created_at', String)   
    
    def __init__(self, user_id, total):
        self.user_id = user_id
        self.total = total
        self.created_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


agent.commit()

# Base.metadata.create_all(engine)


# category = agent.query(Category).all()
    
# categoryname = []
# category_product_count = []

# for i in range(len(category)):
#     categoryname.append(category[i].name)
#     category_product_count.append(len(agent.query(Product).filter(Product.category == category[i].name).all()))


# print(categoryname)
# print(category_product_count)  