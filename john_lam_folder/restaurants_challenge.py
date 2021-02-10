print("Challenge: Favourite Restaurants")

print()

print("Question 1")

print("Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. Go through the dictionary and print out the following 3 pieces of information about the restaurant: \n1. The latitude and longitude of Four Barrel Coffee \n2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. \n3. The website of Four Barrel Coffee.")

restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}

print(restaurant)

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.

print(f'The latitude and longitude of Four Barrel Coffee is {restaurant["latitude"]}, {restaurant["longitude"]}')

# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.

print(f'the complete address of the Four Barrel Coffee is {restaurant["address1"]}, {restaurant["city"]}, {restaurant["state"]} {restaurant["zip_code"]}')

# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print(f'The website of Four Barrel Coffee is {restaurant["url"]}')

print()

print("Question 2")

# TODO: Create a new empty dictionary called fav_restaurants.

# fav_restaurants = {
#     "five guys": ["123 main street, Larkspar, NY 93421", "hamburger", "12am - 11pm"],
#     "Louis & Earnie's Pizza": ["231 bird street, Ontario, NY 17231", "10am - 2pm"],
#     "Rocket" : ["12 Bird Island, What, NY 18237", "fried Chicken", "opens 24 Hours!"]
#  }



# TODO: Choose 3 of your most favourite restaurants in NYC and add the following information for those restaurants inside fav_restaurants:
#         1. Name of the restaurant - Should be the key of the dictionary
#         2. Address of the restaurant - 1st value of the list
#         3. Favourite dish in that restaurant - 2nd value of the list
#         4. Opening and closing hours of that restaurant - 3rd value of the list
# TODO: Print the dictionary.

'''
The below code makes a dictionary called fav_restaurants and stores three keys representing my favorite restraunts. The values are stored in a list that has the restaurants address, my favorite dish and operating hours

'''

fav_restaurants = {"five guys" :["Address: 123 main street, Larkspar, NY 93421.", "My favorite dish is Cheeseburgers", "The hours of operation are from 12:00am to 1:00pm"],
                   "Chinese Palace" :["Address: 21 Jump Street, Ontario, NY 81237.", "My favorite dish is Emperor Chicken.", "The hours of operation are from 12:00am to 11:59pm"],
                   "Japanese Pagoda" : ["Address: 38 Sesame Street, Yonkers, NY 18237.", "The hours of operation are from 11:00 am to 10:00pm"]

}

print(fav_restaurants)


# The dictionary should look like this

'''
fav_restaurants =
{
    "Subway": ["116th & Broadway, NY 10016", "Pizza Sub", "12 PM - 12 AM"]
    "Dominoes": []
    and so on....
}
'''

print()

print("Question 3")

print("Imagine that any 1 of your most favourite restaurants closed down during Covid. Remove the details of that restaurant from the dictionary fav_restaurants.")

# TODO: Remove 1 restaurant from the dictionary fav_restaurants.

fav_restaurants.pop("five guys")

print(fav_restaurants)

# TODO: Print the new dictionary. The new dictionary should contain only 2 restaurants.

print()

print("Question 4")

print("Imagine that another one of your most favourite restaurants modified its opening and closing hours during Covid. Update just the hours field (3rd value of the list) for 1 restaurant in the dictionary fav_restaurants.")

# TODO: Update the hours field of 1 restaurant in the dictionary fav_restaurants.

old_hours = fav_restaurants["Chinese Palace"][2]

fav_restaurants["Chinese Palace"][2] = "The hours of operation are from 7:00am to 7:00pm"

new_hours = fav_restaurants["Chinese Palace"][2]

# TODO: Print the old and new open hours of the restaurant by accessing those fields from the dictionary.

print(old_hours)
print(new_hours)

# TODO: Print the updated dictionary.

print(fav_restaurants)

# Question #4 is a real doosy