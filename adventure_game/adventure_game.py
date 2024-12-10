name = input("Type your name:" )
print("Welcome,", name, "to this adventure")

answer = input("You are on dirt road, it has to come to an end and you can go left or right. Which way would you like to go?"). lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across ")
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("You walk for many miles, ran out of water and you lost the game ")
    else:
        print("Not valid option. You lose. ")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back(cross/back)")
    if answer == "cross":
        answer = input("On your road appeared a bandit and he want's 10 gold coins for crossing him bridge. What are you doing? (pay/fight)")
        if answer == "pay":
            print("Bandit is assassinating you suddenly during paying him. You lose")
        elif answer == "fight":
            print("You hit the bandit for 20 hp")
            print("You've been hit and lose 10 hp")
            print("You killed bandit. You won")
        
    elif answer == "back":
        print("You walk for many miles, ran out of water and you lost the game ")
    else:
        print("Not valid option. You lose. ")
else:
    print("Not valid option. You lose")
    
print("Thank you adventurer", name)