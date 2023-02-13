from Input import product_catalogue
import product_available_2
import holyday_validation_1
from Input import costumer_details

# This method return the final output in which order is fulfill with
# total price of order condition that is >99  and < 4999

def price_validation():
    price_validation_list2 = product_available_2.create_order()
    product_catalogue1 = product_catalogue()
    price_validation_list = []
    for i in range (len(price_validation_list2)):
        temp_l1 = []
        product_list1 = (price_validation_list2[i])["item_name"]
        quantity_list1 = (price_validation_list2[i])["item_quantity"]
        count = 0
        for j in product_list1:

            for k in range(len(product_catalogue1)):
                var = (product_catalogue1[k])["productName"] == j
                if var == True:

                    total_price = (product_catalogue1[k])["price"]*quantity_list1[count]
                    temp_l1.append(total_price)
                    count +=1
                    break
        sum1 = sum(temp_l1)
        if sum1>99 and sum1<5000:
            (price_validation_list2[i])["Total_Price"] =sum1

            price_validation_list.append(price_validation_list2[i])
        elif sum1 <= 99:
            holyday_validation_1.cancel_order.append(price_validation_list2[i])
            order_id1 = (price_validation_list2[i])["order_id"]
            print( f"Your Order {order_id1} is not placed due to small total bill price ")
        else:
            order_id1 = (price_validation_list2[i])["order_id"]
            holyday_validation_1.cancel_order.append(price_validation_list2[i])
            print(f"Your Order {order_id1} is not placed due to the larger total bill price. ")

    return price_validation_list

def final_order_list():
    dict_3 = price_validation()
    dict_2 = costumer_details()
    Final_Order = []
    for i in dict_3:
        for j in dict_2:
            if i["order_id"] == j["order_id"]:
                temp = i
                temp.update(j)
                Final_Order.append(temp)

    return Final_Order





