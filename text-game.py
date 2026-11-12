print("Welcome to my island! \nThere are two doors in front of you. a red door and a blue door")
opened = str(input("Which door do you want to open?"))

if opened == "blue":
    print("Oops! You chose the crocodile door. \nGame over!")
elif opened == "red":
    print("Great! now you entered a room. \nYou found three boxes: white, black, green")
        
    room = str(input("Which box do you open?"))
    if room == "white":
        print("Oops! You opend a box filled with snakes")
    elif room == "black":
        print("Oops! You opened a box filled with spiders")
    elif room == "green":
        print("Congratulations! You found the treasure!")
    else:
        print("Invalid choice!")
else:
    print("Invalid choice!")
