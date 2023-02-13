import mysql.connector
import json
from price_validation_3 import final_order_list
from update_table import update_function
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Jitendra@1899',
    port='3306',
    database='product_catalogue'
)

d1 = open("costumer_order.json")
costumer_orders = json.load(d1)
cursor = conn.cursor()
for i, item in enumerate(costumer_orders):
    order_id = item.get("order_id")
    item_name = str(item.get("item_name"))
    item_quantity = str(item.get("item_quantity"))
    date = item.get("date")
    temp_set = (order_id, item_name, item_quantity, date)
    cursor.execute("USE product_catalogue")

    com = '''INSERT INTO product_catalogue.costumer_orders (order_id, item_name, item_quantity, date1) VALUES (%s,%s,%s,%s)'''

    cursor.execute(com, temp_set)
    conn.commit()


d = open("costumer_details.json")
costumer_detail = json.load(d)
for i, item in enumerate(costumer_detail):
    id = item.get("order_id")
    email = item.get("costumer_id")
    mobile = item.get("costumer_mo_no")
    TMP = (id, email, mobile)
    cursor.execute("USE product_catalogue")
    com = '''INSERT INTO product_catalogue.costumer_information (ID, EMAIL, MOBILE_NUMBER) VALUES (%s,%s,%s)'''
    cursor.execute(com, TMP)
    conn.commit()


y = open("product_catalogue.json")
product_catalogue1 = json.load(y)
for i, item in enumerate(product_catalogue1):
    product_id = item.get("productId")
    product_name = str(item.get("productName"))
    available_quantity = str(item.get("availableQuantity"))
    price = item.get("price")
    temp_set = (product_id, product_name, available_quantity, price)
    cursor.execute("USE product_catalogue")

    com = '''INSERT INTO product_catalogue.shop (product_id, product_name, available_quantity, product_price) VALUES (%s,%s,%s,%s)'''

    cursor.execute(com, temp_set)
    conn.commit()


cursor = conn.cursor()
for i, item in enumerate(final_order_list()):
    order_id = str(item.get("order_id"))
    item_name = str(item.get("item_name"))
    item_quantity = str(item.get("item_quantity"))
    date = str(item.get("date"))
    total_price = str(item.get("Total_Price"))
    costumer_id = str(item.get("costumer_id"))
    costumer_mo_no = str(item.get("costumer_mo_no"))
    temp_set = (order_id, item_name, item_quantity, date, total_price, costumer_id, costumer_mo_no)
    cursor.execute("USE product_catalogue")

    com = '''INSERT INTO product_catalogue.final_order_placed(order_id, item_name, item_quantity, date, total_Price, costumer_id, costumer_mo_no)
     VALUES (%s,%s,%s,%s,%s,%s,%s)'''

    cursor.execute(com, temp_set)
    conn.commit()

update = update_function()
for i, item in enumerate(update):
    product_id = str(item.get("productId"))
    product_name = str(item.get("productName"))
    available_quantity = str(item.get("availableQuantity"))
    product_price = str(item.get("price"))
    temp_set2 = (product_id, product_name, available_quantity, product_price)
    cursor.execute("USE product_catalogue")

    com1 = '''INSERT INTO product_catalogue.update_table (product_id, product_name, available_quantity, product_price) VALUES (%s,%s,%s,%s)'''

    cursor.execute(com1, temp_set2)
    conn.commit()