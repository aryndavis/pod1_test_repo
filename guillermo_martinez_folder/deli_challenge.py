
print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()

#Found this really cool simplification of calling a function within a list!
meats = [meat.capitalize() for meat in meats]
print(meats)
print()
cheeses = [cheese.capitalize() for cheese in cheeses]
print(cheeses)
print()

# for i in range(len(meats))
#     meats[i] = meats[i].capitalize()
# print(meats)





print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list

# Was difficult for me to do without the combo variable.. 
sandwiches = []
for meat in meats:
    for cheese in cheeses:
        # Must concatenate strings, or else the input will not be read
        combo = meat + ", " + cheese
        sandwiches.append(combo)
print(sandwiches)


   

print()

print('Question 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
# TODO: Loop over the sandwiches list.
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'

s = False
order = input("What kind of sandwich would you like?:")
for sandwich in sandwiches:
    if order == sandwich:
        s = True
        print()
        print(f'Great choice! 1 {order} coming right up!')
        break
if not s:
    print("We no have dat")

#Final version


