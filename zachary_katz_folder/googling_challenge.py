'''
GOOGLING CHALLENGE! 
Today, we'll ask you to write a bunch of small pieces of code.
Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.
So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!
For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''


# 1A. Sort the below list in alphabetical order
print('QUESTION 1\n')
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']
my_friends_reverse = sorted(my_friends)
print(my_friends_reverse)

# Source: https://stackoverflow.com/questions/14032521/python-data-structure-sort-list-alphabetically

# 1B. Comment your code in 1A to convince yourself you understand how it works
# Sorts a list of strings; words that start with uppercase get preference over those that start with lowercase
# Is possible to sort in reverse

# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}

my_account_keys = my_account.keys()
print(my_account_keys)

# 2B. Comment your code in 2A to convince yourself you understand how it works

# No source: I already knew the answer to this one

# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'

wood_count = my_string.count("wood")
print(wood_count)

# 3B. Comment your code in 3A to convince yourself you understand how it works

# No source: I already knew the answer to this one also

# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']

banana_count = my_list.count("banana")
print(banana_count)

# 4B. Comment your code in 4A to convince yourself you understand how it works

# I knew that the "count" method could be applied to both lists and strings already
# Just for fun, I double checked on google, and found this source as well to confirm https://www.w3schools.com/python/ref_list_count.asp 

# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')

unique_list = set(my_list)
print(unique_list)

# Source: https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python

# 5B. Comment your code in 5A to convince yourself you understand how it works

# After declaring your list, you can obtain unique values by converting the list to a set.
# You could also convert it back to a list using list() afterwards as needed

# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')
import numpy as np 
from numpy import random

random_number = random.rand(1)
print(random_number)

# Source documentation here: https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.rand.html#numpy.random.rand

# 6B. Comment your code in 6A to convince yourself you understand how it works


'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 
Remember to comment all your code and push your work to your Github repo when you're done!
'''