'''
Planning & pseudocode challenge!

For each piece here, write out the pseudocode as comments FIRST, then write your code!

At many points, you'll have to choose between using a list vs. dictionary. Justify your choices!
'''


'''
1. Shipping

You are building a system to handle shipping orders. Each order should have 3 pieces of information:
-destination (string) (for the purposes of this challenge this can be any place, no need to make a full address)
-date_shipped (string)
-weight (float) (how many pounds the package is)

Will you choose to make each shipping order as a dictionary or list? Why?

'''
'''
I will choose to use a dictionary because I can store key : values pairs to track values for my keys like destination : address, date_shipped : date, weight: float(weight)
'''
'''

Assign 3 separate orders to 3 separate variables
'''
print('\nPART 1')

order_1 = {'destination': 'Elk Grove', 'date_shipped': 'March 11, 2021', 'weight': float(32)}
order_2 = {'destination': 'Oakland', 'date_shipped': 'April 22, 2021', 'weight': float(25)}
order_3 = {'destination': 'San Diego', 'date_shipped': 'July 12, 2021', 'weight': float(15)}

print(order_1)
print(order_2)
print(order_3)


'''
2. Building the database

Now, let's put the orders all into a database togther (all the orders are stored in 1 variable). 

Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!). 

Print out the database to make sure all the info is in there. 

'''
'''
Create a list and assign it to a variable and index order_1, order_2, order_3
'''

print('\nPART 2')

database = [order_1, order_2, order_3]

print(database)


'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''

'''
1. create a new order_n 
2. write a function that takes a perimeter
3. write code to append the argument to the database
4. return the code to the function
5. call the function and give it the new order as the argument
6. print the new data base
'''
print('\nPART 3')

order_4 = {'destination': 'Oklahoma', 'date_shipped': 'August 19, 2021', 'weight': float(23)}

def add_order(order):
    new_order = database.append(order)
    return new_order

add_order(order_4)

print(database)

'''
4. Define a function called complete_order() to mark a specific order in your database complete

This means you'll need a new piece of data inside the order that is True when the order is complete.

Test this out and print out your database to make sure it works!

HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database

'''

'''

1. Write a function that adds a new key value to all of the orders: key = delivered, value = False
2. define the function complete_order with two perimeters (library and status) library allows you to access the order you are trying to update, status allows you to change it to complete
4. evaluate order to determine the status
5. if status == complete, then update order status to True
6. print newly updated library

'''
#updates database with new key value delivered and set it with a value of False. 
#if an order is "delivered" it is complete

def database_update(library):
    for books in library:
        books["Delivered"] = False
        print(books)

def complete_order(library, status):
    if status == "complete":
       library["Delivered"] = True
       print(library)
    
#function that allows you to update order delivery of a given order


print('\nPART 4')

print(complete_order(database[1], "complete"))

      


