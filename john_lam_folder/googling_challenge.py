'''
GOOGLING CHALLENGE! 

Today, we'll ask you to write a bunch of small pieces of code.

Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.

So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!

For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''
import numpy as np

# 1A. Sort the below list in alphabetical order
print('QUESTION 1\n')
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']

my_friends.sort()

print('Sorted list:', my_friends)

# 1B. Comment your code in 1A to convince yourself you understand how it works

print("The .sort() method took my list and alphabetically reorganized my list. I believe what this function did was to evaluate the value of the first letter of each word then the second letter of each word, and based on the value, the list was reorganized based on the value it had in descending order. I found the solution here: https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-alphabetically/")

# 2A. Get all the keys from the below dictionary, then print them out:

# Hint: there is a single command that can do this
print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}

print(my_account.keys())

# 2B. Comment your code in 2A to convince yourself you understand how it works

print("The .key() method returns all of the keys in a dictionary. I believe what this method did was, to access each key and saved it to a variable and returned it back to the function, hence we get all the keys back from the dictionary. I found the solution here: https://www.geeksforgeeks.org/python-dictionary-keys-method/")

# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'
what = my_string.count("wood")
print(f"The number of times wood appears in the string is {what}. I believe how this is evaluated and returned back with the correct answer is by first performing a split() method on the variable what, to index each word into a list. Once the words are indexed, create a function that takes an arguement of the word we want to compare each value in the list. This can be performed simply by creating a for loop that compares each value to the argument. For the values that are the same as the argument, we save a count of how many times that word appears into a new variable. At the end of the function we return that variable that tells us how many times the argument appears in the list. I found the solution here: https://www.geeksforgeeks.org/python-string-count/#:~:text=count()%20function%20in%20an,substring%20in%20the%20given%20string.&text=Parameters%3A,compulsory%20and%20two%20optional%20parameters.")

# 3B. Comment your code in 3A to convince yourself you understand how it works

# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']

dirty = my_list.count("banana")
print(f"The number of times banana appears in the list is {dirty}. I believe what the method .count did was identical to 3A, with the exception of not having to do a split() method on my_list to began doing the same function as 3A to return the amount of times banana shows up")

# 4B. Comment your code in 4A to convince yourself you understand how it works


# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')


# 5B. Comment your code in 5A to convince yourself you understand how it works

list_set = set(my_list)

print(f"The unique value in my_list are: {list_set}. I believe what the method in this instance did was to create a function that loops over all of the values, comparing one value to the next, and save only 'unique' values to a variable, and return the variable that saved all the 'unique' variables. I found the solution to this problem here: https://www.geeksforgeeks.org/python-get-unique-values-list/#:~:text=Using%20set()%20property%20of,a%20list%20to%20print%20it.")

# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')

rand_num = np.random.normal(0,1)

print(f"The random number between 0 and 1 is: {rand_num}. The library numpy allowed me to use np.random.normal to give it two numbers in a range to return a value. In this instance, I set the first value as the starting value, and 1 as the ending value. What I told the numpy library to do was to return a random value between 0 and 1. With this method, I can pretty much generate any random number with as big of a range as I want. ")

# 6B. Comment your code in 6A to convince yourself you understand how it works

'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 

Remember to comment all your code and push your work to your Github repo when you're done!
'''
