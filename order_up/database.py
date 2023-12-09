from dotenv import load_dotenv
load_dotenv()
# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType,Table




with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")

    beverages = MenuItemType(name = 'Beverages')
    entrees = MenuItemType(name = 'Entrees')
    sides = MenuItemType(name = 'Sides')

    dinner = Menu(name='dinner' )

    fries = MenuItem(name='fries',price=3.50,menu_item_type=sides,menu=dinner)
    drp = MenuItem(name= 'Dr. Pepper',price = 1.0, menu_item_type = beverages,menu = dinner)
    jambalaya = MenuItem(name= 'Jambalaya',price = 21.98, menu_item_type = entrees,menu = dinner)
   
    db.session.add_all([dinner,beverages,entrees,sides,employee])
    db.session.commit()

    for n in range(1,11):
        table = Table(number=n,capacity=n)
        db.session.add(table)
    db.session.commit()