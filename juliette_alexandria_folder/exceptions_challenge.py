print('Question 1')
# TODO: Fix error(s) so that the if/else blocks runs without issues
a = 1
b = 2
if a < b:
    print(f'{a} is less than {b}') #fixed indentation
else:
    print(f'{a} is greater than {b}') #fixed indentation

print('')

print('Question 2')
# TODO: Fix error(s) so that a list of sandwiches with unique combinations of meats and cheeses is printed at line 22

meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

sandwiches = []

for meat in meats: #added ":"
    for cheese in cheeses:
        sandwiches.append(f'{meat} & {cheese}') #fixed type in 'meets'

print(sandwiches)

print('')

print('Question 3')
# TODO: Fix error(s) in the the print statements to repeat a string


def repeat(str, times):
    return str * times


print(repeat('python', 3))
print(repeat('[]', 3))
print(repeat('//', 3))
print(repeat('{}', 5)) #added '' marks
print(repeat('{[', 3))

print('')

print('Question 4')
# TODO: Fix error(s) in the print statements to look up all 5 fruits by their index

fruits = ['apples', 'oranges', 'bananas', 'tomatoes', 'cherries']

print(fruits[0]) #changed index so it starts at 10
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])


print('')

print('Question 5')

num = input("Enter a number to compute it's square value: ")

# Line 65 currently error out if you provide an input like a dictionary instead of a number
# TODO: Rewrite line 65 with try/except blocks to handle all exceptions. If an exception exists, print 'Something Went Wrong!'
# TODO: Bonus: Add a finally block to print 'The End'
try:
    print(int(num) * int(num))
except:
    print('Something Went Wrong!')

print('Question 6')

# TODO: Change the code here so that the 'NameError' exception block runs.
name = 'Yusuf'

try:
    print(Name.capitalize()) #Made variable invalid to trigger exception
except NameError:
    print('You got to run this exception block! Your challenge is completed!')
except:
    print('You should not be seeing this print statement. Try a different solution!')