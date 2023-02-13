from Input import product_catalogue
import holyday_validation_1

data_order = holyday_validation_1.holyday_checking_order()

# First We have stored the total available products and their total quantity.
present_item_list = []
item_availability = {}

object_pc = product_catalogue()
for i in object_pc:
    present_item_list.append(i["productName"])
    temp = {i["productName"]: i["availableQuantity"]}
    item_availability.update(temp)

# ae = 0  # for store boolean value.
# dict_of_stock = []

# This method return the order those are satisfied the available product in product_catalogue and their quantity.
# We should not place those order which demand is more than available quantity.
# we should not place unavailable products order.
def create_order():
    temp_list = []
    final_order = []
    for ii in range(len(data_order)):
        ab = ((data_order[ii])["item_name"])
        ac = ((data_order[ii])["item_quantity"])

        if len(ab)>1 and len(list(ab)) == len(list(ac)):
            d4 = {}
            l4 = []
            for k1 in range(len(ab)):
                k = ab[k1]
                for i in range(len(object_pc)):
                    if k in present_item_list:
                            ae = (object_pc[i])["productName"] == k
                            af = (object_pc[i])
                            if ae == True:
                                update_stock = {k: af["availableQuantity"]}

                                if ac[k1] <= update_stock[k]:
                                    temp_list.append(af)
                                    l4.append(k)
                                    temp1 = {k: update_stock[k] - ac[k1]}
                                    d4.update(temp1)
                                    break



            if len(ab) == len(l4):
                count = 0
                for b in range(len(ab)):
                    item_availability.update(d4)
                    temp_dict = {"availableQuantity": ((temp_list[b])["availableQuantity"] - ac[b])}

                    if temp_dict["availableQuantity"] >= 0:
                        # object_pc[ii].update(temp_dict)
                        item_availability.update(d4)
                        count += 1
                        if count == len(ab):
                            final_order.append(data_order[ii])
                            break
            else:
                holyday_validation_1.cancel_order.append(data_order[ii])

        elif len(ab) == 1:
            if ab[0] in present_item_list:
                for i in range(len(object_pc)):

                    ae = (object_pc[i])["productName"] == ab[0]
                    # print(ab[0])
                    if ae == True:
                        # af = (object_pc[ii])
                        count = 0
                        if ac[0] <= item_availability[ab[0]]:
                            temp_dict = {ab[0]: item_availability[ab[0]] - ac[0]}
                            item_availability.update(temp_dict)

                            final_order.append(data_order[ii])
                            break

            else:
                holyday_validation_1.cancel_order.append(data_order[ii])


    return final_order
# print(create_order())


