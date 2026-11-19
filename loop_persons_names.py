names = input("Enter the names of attendees separted by commas: ")
people = names.split(",")
for person in people:
    print("\n" + person + "\n")
    response = input("Is this person attending? (yes/no): ").lower()
    if response == "yes":
        print("Attendance Confirmed!")
    else:
        print("Attendance not Confirmed!")
    print("------")
