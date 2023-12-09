from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


db = SQLAlchemy()

class Employee(db.Model,UserMixin):
    __tablename__='employees'

    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    employee_number = db.Column(db.Integer(),nullable=False,unique=True)
    hashed_password = db.Column(db.String(255),nullable=False)

    orders = db.relationship('Order', back_populates = 'employee')

    @property
    def password(self):
        return self.hashed_password
    
    @password.setter
    def password(self,password):
        self.hashed_password = generate_password_hash(password)

    def checked_password(self,password):
        return check_password_hash(self.password,password)



class Menu(db.Model):
    __tablename__='menus'

    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(30), nullable=False)

    menu_items = db.relationship('MenuItem',back_populates='menu', cascade = 'all, delete, delete-orphan')


class MenuItem(db.Model):
    __tablename__= 'menu_items'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Float, nullable = False)
    menu_id = db.Column(db.Integer,db.ForeignKey('menus.id'), nullable= False)
    menu_type_id = db.Column(db.Integer,db.ForeignKey('menu_item_types.id'), nullable = False)


    menu = db.relationship('Menu', back_populates = 'menu_items')
    menu_item_type = db.relationship('MenuItemType',back_populates='menu_items')

class MenuItemType(db.Model):
    __tablename__ = 'menu_item_types'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    menu_items = db.relationship('MenuItem', back_populates='menu_item_type', cascade = 'all,delete, delete-orphan')



class Table(db.Model):
    __tablename__ = 'tables'

    id = db.Column(db.Integer, primary_key = True)
    number = db.Column(db.Integer, nullable = False)
    capacity = db.Column(db.Integer, nullable = False)
    
    orders = db.relationship('Order', back_populates = 'table')

    #create a order model which has employee and table id as well boolen open or closed
    # Orderdetail has multiple many items that means one to many with menu item
    #so menuItem need id of order as well.then orderdetails will have an order.id which 
    #will point to the order 

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer,primary_key = True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'),nullable = False)
    table_id = db.Column(db.Integer, db.ForeignKey('tables.id'),nullable = False)
    finished = db.Column(db.Boolean, nullable = False)

    employee = db.relationship('Employee', back_populates = 'orders')
    table = db.relationship('Table', back_populates = 'orders')

    details = db.relationship('OrderDetail', back_populates='order')

class OrderDetail(db.Model):
    __tablename__ = 'order_details'
    id = db.Column(db.Integer, primary_key = True)
    order_id = db.Column(db.Integer,db.ForeignKey('orders.id'), nullable = False)
    menu_item_id = db.Column(db.Integer,db.ForeignKey('menu_items.id'), nullable = False)
   
    order = db.relationship('Order', back_populates='details')
    menu_item = db.relationship('MenuItem', foreign_keys=[menu_item_id])