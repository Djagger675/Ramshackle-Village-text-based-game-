print("Welcome to the Ramshackle Village!")
print("You are an avid traveller who decided to explore this archaic village.")
print("One millionaire decided to invest in your voyage.")
print("You can observe that this village is abandoned. You passed like 2 kilometers and the first thing that you glanced is an old-fashioned house.")
print("As you come close to the door, you are starting to think. Do I need to go inside?")
print("Do you want to go inside?")

doorChoice = input("> ")

if doorChoice == "Yes":
    print("You enter the house.")
    print("You see the house is almost empty; however, there is one table with a bottle of Vodka on it.")
    print("Do you want to drink the Vodka?")
    
    vodkaChoice = input("> ")
    
    if vodkaChoice == "Yes":
        print("You drink the Vodka.")
        print("It was spoiled, and now you are dead.")
        print("GAME OVER")
        
    elif vodkaChoice == "No":
        print("You decide not to drink the Vodka.")
        print("You turn around and leave the house.")
else:
    print("You decide to run to another place.")
    print("GAME OVER")

    

