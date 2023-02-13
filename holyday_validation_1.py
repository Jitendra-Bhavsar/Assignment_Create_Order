from Input import costumer_order
from datetime import datetime
import holidays


holyday_validation_list1 = costumer_order()
cancel_order = []

'''this method is first stage of our program
where we have cancelled those order which have ordered on holiday and sunday.
and then pass the return of the method to product available class.'''


def holyday_checking_order():
    holyday_validation_list3 = []

    india = holidays.India()
    for i in holyday_validation_list1:
        temp_date = i["date"]
        temp_date = datetime.strptime(temp_date, '%d-%m-%y')
        if temp_date in india:
            # print("Sry Your Order is not placed due to festival")
            cancel_order.append(i)
        elif temp_date.isoweekday() == 7:
            order_id = i["order_id"]
            # print(f"Sry {order_id} your Order is not placed Due to sunday on {temp_date} ")
            cancel_order.append(i)
        else:
            holyday_validation_list3.append(i)
    return holyday_validation_list3
