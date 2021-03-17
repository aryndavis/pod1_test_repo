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

I would choose a dictionary to later access information through keys rather than memorizing my indexes

Assign 3 separate orders to 3 separate variables

'''
print('\nPART 1')

order_1 = {'Location': 'New York', 'Date': '03/11/2021', 'Weight': 5.0}
order_2 = {'Location': 'Los Angeles', 'Date': '02/15/2021', 'Weight': 3.6}
order_3 = {'Location': 'Texas', 'Date': '01/11/2021','Weight': 9.2}



'''
2. Building the database

Now, let's put the orders all into a database togther (all the orders are stored in 1 variable). 

Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!). 

Print out the database to make sure all the info is in there. 

'''
print('\nPART 2')

database = []
database.append(order_1)
database.append(order_2)
database.append(order_3)
print(database)


'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')

def add_order(new_order):
    database.append(new_order)
    print(database)

add_order({'Location': 'Maine', 'Date': '05/11/2020', 'Weight': 6.2})
    
    
'''
4. Define a function called complete_order() to mark a specific order in your database complete

This means you'll need a new piece of data inside the order that is True when the order is complete.

Test this out and print out your database to make sure it works!

HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
print('\nPART 4')

def complete_order(database, index):
    database[index]['completed'] = True
    print(database[index])

complete_order(database, 0)

    


