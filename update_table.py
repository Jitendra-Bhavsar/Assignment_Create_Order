from price_validation_3 import final_order_list
from Input import product_catalogue

final_list = final_order_list()
product_catalogue3 = product_catalogue()
pc4 = product_catalogue()

def update_function():
    for i in final_list:
        ab = i
        l1 = list(ab.get("item_name"))
        l2 = list(ab.get("item_quantity"))
        if len(l1)>1:
            for j in range(len(l1)):
                for k in range(len(product_catalogue3)):
                    check = l1[j] == (product_catalogue3[k])["productName"]
                    if check == True:
                        temp = {"availableQuantity": ((pc4[k])["availableQuantity"]) - l2[j]}
                        pc4[k].update(temp)
                        break
        else:
            for k in range(len(product_catalogue3)):
                check = l1[0] == (product_catalogue3[k])["productName"]
                if check == True:
                    temp = {"availableQuantity": ((pc4[k])["availableQuantity"]) - l2[0]}
                    pc4[k].update(temp)
                    break


    return pc4

<<<<<<< HEAD
print("Update Product Catalogue: ",update_function())
=======
print("Update_Product_Catalogue: ",update_function())

>>>>>>> b8d10fb (first Assignment)

