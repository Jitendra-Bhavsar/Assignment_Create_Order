
## Q.1) What is the problem statement?
Ans:
The Popular company has decided to launched a new website and mobile application for online groceries shopping. 
All things in technology implementation are done except order service where we need your help. In order service we need an API which can accept orders and save them to database. Choose your favourite database, design database schema (refer any available online groceries website). 
Please refer below additional details.

APIs requirement:
1. Create order.
2. Get order by id.
3. Update order status.

The minimum acceptance criteria:
1. Don't accept orders on public holidays and Sunday.
2. Minimum order amount must be greater than equal to 99 rupees.
3. Maximum order amount should not exceed 4999 rupees.
4. The product must be available to book. Use product catalogue details to check availability quantity.

## Building Steps:-
1) I have created 3 json files as a input (product_catalogue, costuer_detail, costumer_order)
2) To read all json files i have created Input module.
### minimum acceptance criteria:
4) To reject the order which will get on public indian holyday and sunday, I have created holyday_validation_1 module.
5) To satisfied condition 2nd and 3rd  I have created price_validation_3 module.
6) To satisfied the 4th number criteria i have created product_available_2 module.
7) and after all three module run we will get final order list in Output module.
8) after getting final order list we can pass the list to update_table module to update our product catalugue.
9) When you run the update_table module, you can see the update stock of the product after order placed.  """
