print("Challenge 2.1:")
jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37 

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
jamal_murray_3pts_attempt = 93
fred_vanvleet_3pts_attempt = 110
james_harden_3pts_attempt = 109 

print("Challenge 2.4: Build on your print statement")
print(f"In the 2020 NBA playoffs, Jamal Murray attempted {jamal_murray_3pts_attempt} 3 point shots and made {jamal_murray_3pts_made} of them.")
print(f"In the 2020 NBA playoffs, Fred VanVleet attempted {fred_vanvleet_3pts_attempt} 3 point shots and made {fred_vanvleet_3pts_made} of them.")
print(f"In the 2020 NBA playoffs, James Harden attempted {james_harden_3pts_attempt} 3 point shots and made {james_harden_3pts_made} of them.")

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
jamal_murray_3pt_percent = jamal_murray_3pts_made/jamal_murray_3pts_attempt
fred_vanvleet_3pt_percent = fred_vanvleet_3pts_made/fred_vanvleet_3pts_attempt
james_harden_3pt_percent = james_harden_3pts_made/james_harden_3pts_attempt
print(f"In the 2020 NBA playoffs, Jama Murray's 3 point percentage was {jamal_murray_3pt_percent}")
print(f"In the 2020 NBA playoffs, Fred VanVleet's 3 point percentage was {fred_vanvleet_3pt_percent}")
print(f"In the 2020 NBA playoffs, James Harden's 3 point percentage was {james_harden_3pt_percent}")

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
print('The Lakers went all in this offseason and swung a deal for former \
Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram,\
Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \
\nThose three have made good developments with the Pelicans, especially \
Brandon Ingram. \nBut the deal is still a huge win for the Lakers as Lebron\
, Davis, and company have put together an incredible season. \nLos Angeles \
has ridden James and Davis, along with a supporting cast built around them, \
to the second-best record in the NBA. \nThe Lakers ended the season atop\
the Western Conference with a record of 49-14. \nThey were narrowly behind \
the Bucks for the best record in the league. \nDavis proved to the final \
piece necessary for the Lakers to rebound from missing the playoffís last \
year. \nLos Angeles was a dominant club on both sides of the ball and are \
in a position to have another successful year next season.')

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
paragraph = 'The Lakers went all in this offseason and swung a deal for former \
Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram,\
Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \
\nThose three have made good developments with the Pelicans, especially \
Brandon Ingram. \nBut the deal is still a huge win for the Lakers as Lebron\
, Davis, and company have put together an incredible season. \nLos Angeles \
has ridden James and Davis, along with a supporting cast built around them, \
to the second-best record in the NBA. \nThe Lakers ended the season atop\
the Western Conference with a record of 49-14. \nThey were narrowly behind \
the Bucks for the best record in the league. \nDavis proved to the final \
piece necessary for the Lakers to rebound from missing the playoffís last \
year. \nLos Angeles was a dominant club on both sides of the ball and are \
in a position to have another successful year next season. '

print(paragraph.upper())

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
lakers_are_the_best_team = False
print(f'If someone tells you that the Lakers are the best NBA team, that statement is {lakers_are_the_best_team}.')

print('Challenge 3.4: Type Conversion')
print(int(lakers_are_the_best_team))
print(float(lakers_are_the_best_team))

print('Challenge 3.5: Type Conversion Part 2')
print(int(jamal_murray_3pt_percent))
print(int(fred_vanvleet_3pt_percent))
print(int(james_harden_3pt_percent))
