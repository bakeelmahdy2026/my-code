color = []
a = str(input("Add the first color you like: "))
color.append(a)
b = str(input("Do you want to more color? Yes, or No ")).lower()
if b == "yes":
    c = str(input("Add another color to the list: "))
    color.append(c)
    print("The colors you like are:")
    print(color)
else:
    print("The colors you like are:")
    print(color)

    
