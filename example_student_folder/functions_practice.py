# built in functions

# func()
print('This only shows up in console')
type('the type is a string')
float(54)
int(34.0)
str({})
range(100)

# object.func() or methods
text = 'hello world'
text.upper() # .upper() is a string method

integers = [1, 2]
integers.append(3) # .append() is a list method


# custom functions
def hello(first_name, last_name):
    print('hi') # this will run
    return f"Hello World! It's {first_name} {last_name}" # this is the output of the function
    print('bye') # this will not run


print(hello('Ash', 'Rahman'))
print(hello('Paul', 'Bloom'))
print(hello('Alanna', 'Kelly'))

# create a custom function called 'add'
# add(2, 2) -> gives you an output of 4

def add(a, b): # naming the function and the inputs
    # body of the function, where we compute an output
    return a + b

print(add(2, 2))

# create a custom function called 'multiply'
# multiply(3, 3) -> gives you an output of 9
def multiply(a, b):
    return a * b

print(add(multiply(multiply(2, 3), 2), 12))

# complicated logic with functions!
def square_list(nums_list):
    squared_nums = [] 
    # loop over the nums_list input
    for num in nums_list:
        # calculate the square of num
        squared = num * num 
        # add it to squared_nums list
        squared_nums.append(squared)
    return squared_nums # the function's output!

nums = [1, 2, 3, 4, 5]
# store the returned output
squared_output_list = square_list(nums)
# print that output
print(squared_output_list)