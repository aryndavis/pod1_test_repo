print("Challenge 2.1:")
# Create variable here for number of 3 pt shots made by Jamal Murray
jamal_murray_3pts_made = 46
# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
VanVleet_3pts_made = 43
# TODO: Create variable here for number of 3 pt shots made by James Harden
Harden_3pts_made = 37


print("Challenge 2.2:")
# Create print statement here for Jamal Murray
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
# TODO: Create print statement here for Fred VanVleet
print(f"In the 2020 NBA playoffs, Fred Vanvleet made {VanVleet_3pts_made} 3 point shots")
# TODO: Create print statement here for James Harden
print(f"In the 2020 NBA playoffs, James Harden made {Harden_3pts_made} 3 point shots")



print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# TODO: Create variable here for number of 3 pt shot attempts by Jamal Murray
Murray_3pts_attempts = 93
# TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
Vanvleet_3pts_attempts = 110
# TODO: Create variable here for number of 3 pt shot attempts by James Harden
Harden_3pts_attempts = 109


print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and made {Murray_3pts_attempts} attempts.")
print(f"In the 2020 NBA playoffs, Fred Vanvleet made {VanVleet_3pts_made} 3 point shots and made {Vanvleet_3pts_attempts} attempts.")
print(f"In the 2020 NBA playoffs, James Harden made {Harden_3pts_made} 3 point shots and made {Harden_3pts_attempts} attempts.")
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."


print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# TODO: Calculate and print the 3 point percentage for Jamal Murray
print(f"Jamal Murray's 3 pt percentage is {jamal_murray_3pts_made/Murray_3pts_attempts}")
# TODO: Calculate and print the 3 point percentage for Fred VanVleet
print(f"Fred Vanvleet's 3 pt percentage is {VanVleet_3pts_made/Vanvleet_3pts_attempts}")
# TODO: Calculate and print the 3 point percentage for James Harden
print(f"James Harden's 3 pt percentage is {Harden_3pts_made/Harden_3pts_attempts}")
print()

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
long_text = "The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \n They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \n Those three have made good developments with the Pelicans, especially Brandon Ingram. \n But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \n Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \n The Lakers ended the season atop the Western Conference with a record of 49-14. \n They were narrowly behind the Bucks for the best record in the league. \n Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \n Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season."


# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line
print(long_text)

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case
print(long_text.upper())

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
lakers_are_best = True 
print(f"The Lakers are the best team and that answer is {lakers_are_best}.")
# TODO: print out the variable in an f-string to convey your opinion on the lakers

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
print(int(lakers_are_best))
# TODO: Convert your `lakers_are best` variable to a float, and print it out
print(float(lakers_are_best))

print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
Vanvleet_percentage = VanVleet_3pts_made/Vanvleet_3pts_attempts
print(str(Vanvleet_percentage))
Murray_percentage = jamal_murray_3pts_made/Murray_3pts_attempts
print(str(Murray_percentage))
harden_percentage = Harden_3pts_made/Harden_3pts_attempts
print(str(harden_percentage))
# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
print(int(Vanvleet_percentage))
print(int(Murray_percentage))
print(int(harden_percentage))

