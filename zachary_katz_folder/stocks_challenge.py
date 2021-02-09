print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
client_name = input("What's your name?")
client_savings = int(input("How much do you have saved?"))
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

if stock == "amzn":
    price = amazon
    num_of_stocks = round(client_savings/price)
elif stock == "aapl":
    price = apple
    num_of_stocks = round(client_savings/price)
elif stock == "fb":
    price = fb
    num_of_stocks = round(client_savings/price)
elif stock == "goog":
    price = google
    num_of_stocks = round(client_savings/price)
elif stock == "msft":
    price = msft
    num_of_stocks = round(client_savings/price)
else:
    price = "N/A"

print(f"{client_name} has ${client_savings} in savings and he can buy {num_of_stocks} shares of {stock} at the current price of ${price}.")