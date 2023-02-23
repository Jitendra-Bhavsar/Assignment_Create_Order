from Input import costumer_order
from datetime import datetime
import holidays


holiday_validation_list1 = costumer_order()
cancel_order = []

'''this method is first stage of our program
where we have cancelled those order which have ordered on public indian holiday  and sunday 
and return the list holiday_validation_list3.
and then passed holiday_validation_list3 to product_available_2 module.'''


def holiday_checking_order():
    holiday_validation_list3 = []

    india = holidays.India()
    for i in holiday_validation_list1:
        temp_date = i["date"]
        temp_date = datetime.strptime(temp_date, '%d-%m-%y')
        if temp_date in india:
            # print("Sry Your Order is not placed due to indian holiday")
            cancel_order.append(i)
        elif temp_date.isoweekday() == 7:
            order_id = i["order_id"]
            # print(f"Sry {order_id} your Order is not placed Due to sunday on {temp_date} ")
            cancel_order.append(i)
        else:
            holiday_validation_list3.append(i)
    return holiday_validation_list3
