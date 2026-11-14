import random
print("Welcome to 'whose wallet?'")
print("You will give me a list of names, and I will pick a person to pay")
names = input("If your're ready, enter the names separated by a comma ")
name = names.split(",")
lenght_names = len(name) -1
random_number = random.randint(0,lenght_names)
random_person = name[random_number]
print("Please ask " + "' " + random_person + " '" + " to take his wallet out. Dinner is on him")
