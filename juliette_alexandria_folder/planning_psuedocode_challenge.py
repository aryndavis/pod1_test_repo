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

Assign 3 separate orders to 3 separate variables
'''
print('\nPART 1')

#First make 3 orders (dictionaries) with 3 separate key/value pairs (destination, shipped, weight)
order1 ={'destination': 'Eugene', 'shipped': '3/12/21', 'weight': '3.5'}
order2 ={'destination': 'Portland', 'shipped': '3/11/21', 'weight': '10.2'}
order3 ={'destination': 'Salem', 'shipped': '3/13/21', 'weight': '17.87'}
'''
2. Building the database
Now, let's put the orders all into a database togther (all the orders are stored in 1 variable). 
Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!). 
Print out the database to make sure all the info is in there. 
'''
print('\nPART 2')
#create a variable(list) of all the orders - each order is a index item in the list - then print

order_list = [order1, order2, order3]

#print order database
print(order_list)

'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')
#Create new order (dictionary)
#Define a function (add_order) function will have the variable name as the parameter
    #append the order to the database
#Call the add_order function
#Print the order_list

order4 ={'destination': 'Roseburg', 'shipped': '3/14/21', 'weight': '4.3'}


def add_order(order_list, order):
    order_list.append(order)
add_order(order_list, order4)
print(order_list)


'''
4. Define a function called complete_order() to mark a specific order in your database complete
This means you'll need a new piece of data inside the order that is True when the order is complete.
Test this out and print out your database to make sure it works!
HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
print('\nPART 4')

#Define a function called complete_order() to add the "True" value to the completed order's dictionary

def complete_order(order_list, order_index):
    order_list[order_index]['complete'] = True

complete_order(order_list, 2)
print(order_list)

