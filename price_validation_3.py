from Input import product_catalogue
import product_available_2
import holiday_validation_1
from Input import costumer_details

'''price_validation method return the price_validation_list output in which order is fulfill with
total price of order criteria and that is total_order >99  and < 4999'''


def price_validation():
    price_validation_list2 = product_available_2.product_availability()
    product_catalogue1 = product_catalogue()
    price_validation_list = []
    for i in range(len(price_validation_list2)):
        temp_l1 = []
        product_list1 = (price_validation_list2[i])["item_name"]
        quantity_list1 = (price_validation_list2[i])["item_quantity"]
        count = 0
        for j in product_list1:

            for k in range(len(product_catalogue1)):
                var = (product_catalogue1[k])["productName"] == j
                if var == True:
                    total_price = (product_catalogue1[k])["price"] * quantity_list1[count]
                    temp_l1.append(total_price)
                    count += 1
                    break
        sum1 = sum(temp_l1)
        if sum1 > 99 and sum1 < 5000:
            (price_validation_list2[i])["Total_Price"] = sum1

            price_validation_list.append(price_validation_list2[i])
        elif sum1 <= 99:
            holiday_validation_1.cancel_order.append(price_validation_list2[i])
            order_id1 = (price_validation_list2[i])["order_id"]
            print(f"Your Order {order_id1} is not placed due to small total bill price ")
        else:
            order_id1 = (price_validation_list2[i])["order_id"]
            holiday_validation_1.cancel_order.append(price_validation_list2[i])
            print(f"Your Order {order_id1} is not placed due to the larger total bill price. ")

    return price_validation_list


print(price_validation())
'''method offer_apply is return the offer_apply_list.
1) one order can used only one offer not more than one.
2) '''


def offer_apply():
    offer_apply_list = []
    price_validation_list = price_validation()
    product_catalogue2 = product_catalogue()

    '''This for loop is for flat discount on specific product'''

    for i in price_validation_list:
        temp_list = i['item_name']
        for j in range(len(temp_list)):
            if temp_list[j] == 'Rice':
                number_Quantity = i["item_quantity"][j]
                if number_Quantity > 3:
                    for k in product_catalogue2:

                        if k["productName"] == "Rice":
                            price = i['Total_Price'] - number_Quantity * k['price'] * 0.30
                            i["Total_Price"] = price
                            offer_apply_list.append(i)
                            break
                    break


        else:
            if i["Total_Price"] > 2000:
                price = i["Total_Price"] - i["Total_Price"] * 0.05
                i["Total_Price"] = price
                offer_apply_list.append(i)
            else:
                offer_apply_list.append(i)
    '''This else loop is for discount on order amount criteria is >2000'''
    return offer_apply_list


# print(offer_apply())

'''final_order_list method is return concat of the price_validation dict and costumer_details dict.'''


def final_order_list():
    dict_3 = offer_apply()
    dict_2 = costumer_details()
    Final_Order = []
    for i in dict_3:
        for j in dict_2:
            if i["order_id"] == j["order_id"]:
                temp = i
                temp.update(j)
                Final_Order.append(temp)

    return Final_Order


# print(final_order_list())




