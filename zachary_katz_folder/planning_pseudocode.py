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

# Each shipping order will be a dictionary, with three key/value pairs each (destination, shipping date, and weight are keys)
order_num1 = {'destination':'New York City', 'date_shipped': '1/2/03', 'weight': 1.23}
order_num2 = {'destination':'Los Angeles', 'date_shipped': '4/5/06', 'weight': 4.56}
order_num3 = {'destination':'Chicago', 'date_shipped': '7/8/09', 'weight': 7.89}



'''
2. Building the database
Now, let's put the orders all into a database togther (all the orders are storedin 1 variable). 
Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!). 
Print out the database to make sure all the info is in there. 
'''
print('\nPART 2')


# The easiest way to approach this is to create a list, where each list element is one of three orders
# Then, assign list to a new variable

order_database_list = [order_num1, order_num2, order_num3]

# Print database
print(order_database_list)

'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')

# Make some new orders
order_num4 = {'destination':'Philadelphia', 'date_shipped': '2/2/21', 'weight': 3.67}
order_num5 = {'destination':'Seattle', 'date_shipped': '3/10/21', 'weight': 4.78}


# Defining function to take two args, database and new order
def add_order_to_list(database, order):
	# inside the function, append the order dict to the end of the list
	database.append(order)

# test out calling the functino to add order4 and order5
add_order_to_list(order_database_list, order_num4)
add_order_to_list(order_database_list, order_num5)

# check database by printing it out
print(order_database_list)

'''
4. Define a function called complete_order() to mark a specific order in your database complete
This means you'll need a new piece of data inside the order that is True when the order is complete.
Test this out and print out your database to make sure it works!
HINT: Think about how your choice of list/dictionary in number 2 informs how someone would reference an order in the database
'''
print('\nPART 4')


# LIST SOLUTION
# Referencing orders by list position, i.e. index
# Define function to accept 2 arguments, database and index corresponding to completed order
def complete_order_list(database, order_index):
	# go to the corresponding order in the list, then make a key called 'complete' and set it to True
	database[order_index]['Completed'] = True

# Test on indices 1 and 2, which are orders 2 and 3
complete_order_list(order_database_list, 1)
complete_order_list(order_database_list, 3)

# print out to check it
print(order_database_list)