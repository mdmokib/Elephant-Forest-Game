print('''
   ,-"""""--,-"")    (""-,--"""""-.
    :|        \; '|    |' :/        |:
    ;| :",_,: : "\|  `-|;" : :,_,": |;
ctr  |_||   |_|   J    L   |_|   ||_|
''')
print("Welcome to Forest.")
print("Your mission is to find the banana garden.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a field. There is an garden at the end of three field. Type "wait" to wait for an another elephant. Type "run" to run alone. \n').lower()
  if choice2 == "wait":
    choice3 = input("You got a friend for company. There are 3 roads. One straight, one left and one right. Which road do you choose? \n").lower()
    if choice3 == "left":
      print("It's a muddy road. You can not go. Game Over.")
    elif choice3 == "right":
      print("You found banana garden! You can eat!")
    elif choice3 == "straight":
      print("You enter a blocked road. Game Over.")
    else:
      print("You chose a raod that doesn't exist. Game Over.")
  else:
    print("You get attacked by the bad people. Game Over.")
else:
  print("You fell into pond. Game Over.")