from sqlalchemy import create_engine, Column, Integer, String, update, delete
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.sqlite3', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name',String)
    email = Column('email',String)
    password = Column('password', String)
    admin = Column('admin', Integer, default=0)
    
    def __init__(self, name, email,password):
        self.name = name
        self.email = email
        self.password = password
    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.email, self.password)    


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
    
    def __init__(self, user_id, product_id, product_name, quantity, price, created_at):
        self.user_id = user_id
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.created_at = created_at




class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer)
    amount = Column('amount', Integer)
    date = Column('date', String)
    
    def __init__(self, user_id, amount, date):
        self.user_id = user_id
        self.amount = amount
        self.date = date
        

session.query(Order).filter(Order.amount == 4000).update({Order.amount: 5000, Order.date: '2022-10-10'})

session.commit()

# Base.metadata.create_all(engine)


# session = Session()
# product = session.query(Product).filter(Product.id == 1).first()
# all_product = session.query(Product).all()

# print(product)
# # product = Product('test', 'test', 1, 1, 'test', 'test')

# # session.add(product)
# pro = Product('Kiwi', 'Fruit','', 210, 26, '', 'kiwi.jpeg')

# session.add(pro)   
# session.commit()
# session.commit()
# product = session.query(Product).all()

# for i in product:
#     print(i.name)


# c1 = Category('Fruit', 'fruit.jpeg', '2019-10-10')

# session.add(c1)
# session.commit()

# row = session.query(Category).filter(Category.id == 3).first()

# print(row.name)
# print(row.image)
# print(row.date)    


