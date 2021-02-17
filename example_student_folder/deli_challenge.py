
print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()
for i in range(len(meats)):
    print(i, meats[i])
    meats[i] = meats[i].capitalize()

print(meats)

for i in range(len(cheeses)):
    cheeses[i] = cheeses[i].capitalize()

print(cheeses)

print()

print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list
sandwiches = []


for cheese in cheeses:
    for meat in meats:
        sandwiches.append(f"{cheese} & {meat}")

print(sandwiches)
print()

print('Question 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
# TODO: Loop over the sandwiches list.
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'

order = input("What sandwich would you like? ")
found = False
for sandwich in sandwiches:
    #print(sandwich)
    if order.lower() == sandwich.lower():
        print(f'Great choice! 1 {order} coming right up!')
        found = True
        break
    
if found == False:
    print("Sorry, that doesn't exist")

