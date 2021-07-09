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

#https://www.w3schools.com/python/ref_func_sorted.asp - sorts the list in alphabetical order - creates a new variable by applying the sorted function to my_friends variable
friends_sorted = sorted(my_friends)
print(friends_sorted)

# 1B. Comment your code in 1A to convince yourself you understand how it works


# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}

# 2B. Comment your code in 2A to convince yourself you understand how it works

# https://www.tutorialspoint.com/python/dictionary_keys.htm - Prints all keys in given dictionary

print(my_account.keys())



# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'


# 3B. Comment your code in 3A to convince yourself you understand how it works

# https://www.programiz.com/python-programming/methods/string/count - count() function searches the main string and counts how many times a defined substring occurs then returns the number
substring = 'wood'

print(my_string.count(substring))



# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']


# 4B. Comment your code in 4A to convince yourself you understand how it works

#https://www.kite.com/python/answers/how-to-count-the-number-of-occurrences-of-an-element-in-a-list-in-python - Same count function as previous question, just applied to a list. Searches the list items and returns the number of occurences of the given value

print(my_list.count('banana'))


# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')


# 5B. Comment your code in 5A to convince yourself you understand how it works
# https://www.delftstack.com/howto/python/python-count-unique-values-in-list/#use-numpy-unique-to-count-the-unique-values-in-python-list - import numpy, use numpy.unique technique to identify the unique occurences of strings in the variable

print(np.unique(my_list))


# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')


# 6B. Comment your code in 6A to convince yourself you understand how it works
# https://chrisalbon.com/python/basics/generating_random_numbers_with_numpy/ - define the range of numbers (low and high parameters) and the number of items in the array it should return (size)

print(np.random.randint(low=0, high=1, size=1))


'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 
Remember to comment all your code and push your work to your Github repo when you're done!
'''