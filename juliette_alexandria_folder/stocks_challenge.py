print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
name = input("What is your name?")
print(name)
# TODO: Write code to ask the client his savings and save it to another variable.
saving = input("How much savings do you have?")
print(saving)
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amazon' for Amazon, 'apple' for Apple, 'fb' for Facebook, 'google' for Google and 'msft' for Microsoft.")
print(stock)

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

#Cconverted saving string to an integter for calculations

savings = (int(saving))


if stock == "amazon":
    amazonshares = (savings / amazon)
elif stock == "apple":
    appleshares = (savings / apple)
elif stock == "fb":
    fbshares = (savings / fb)
elif stock == "google":
    googleshares = (savings / google)
elif stock == "msft":
    microshares = (savings / msft)
else:
    print("You did not enter a valid stock name")      

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

if stock == "amazon":
    print(f"{name} has ${savings} and can buy {amazonshares} shares of Amazon at the current price of $3000.")
elif stock == "apple":
    print(f"{name} has ${savings} and can buy {appleshares} shares of Apple at the current price of $100.")
elif stock == "fb":
    print(f"{name} has ${savings} and can buy {fbshares} shares of Facebook at the current price of $250.")
elif stock == "google":
    print(f"{name} has ${savings} and can buy {googleshares} shares of Google at the current price of $1400.")
elif stock == "msft":
    print(f"{name} has ${savings} and can buy {microshares} shares of Microsoft at the current price of $200.")
else:
    print("You did not give the correct information to provide you with an answer") 

