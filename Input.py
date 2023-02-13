import json

def costumer_order():
    d1 = open("costumer_order.json")

    costumer_orders = json.load(d1)

    return costumer_orders

def costumer_details():
    d = open("costumer_details.json")

    costumer_detail = json.load(d)

    return costumer_detail

def product_catalogue():

    y = open("product_catalogue.json")

    product_catalogue1 = json.load(y)

    return product_catalogue1

