from price_validation_3 import final_order_list
from update_table import update_function
import pandas as pd

class My_Output:
    def my_output(self):
        output = final_order_list()

        return output
obj = My_Output()
# print the list of placed order.
print("Final_Placed_Order_List: ",pd.DataFrame(obj.my_output()))
# To see update product catalogue
print("Update Product_catalogue: ",pd.DataFrame(update_function()))

"""
1) When you run this output module You get list of
placed order(costumer_order, costumer_detail), update product catalogue in mysql database.
2) you can see the output of code in run window also using uncomment the print statement given above.
3) All given validation is completed like as below
  i) order is not accept on public holiday and sunday (holyday_module_1 module).
  ii) order total price must be greater then 99 and less than 4999 (price_validation_3 module).
  iii) order items must be available in shop (product_available_2 module) and order quantity must be less or equal as compare to item_availabily   
4) if code is bug then go to mysql database and truncate all tables and then run.
5) if you not see availableQuantity and price in update product catalogue then you need to see in database mysql you will get. 
"""