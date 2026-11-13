library = []
wishlist = []
book_name = input("Enter the name of a book you own: ")
library.append(book_name)
another_book_name = input("Enter the name of book you own (or press 'Enter' to skip: ")
if another_book_name:
    library.append(another_book_name)
print("\nYour Library: ", library)
c = input("\nEnter the name of a book you wish to have in the future: ")
wishlist.append(c)
d = input("Enter the name of another book you wish to have (or press 'Enter' to skip: ")
if d:
    wishlist.append(d)
print("Your wishlist: ", wishlist)
acquired = input("\nEnter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip: ")
if acquired in wishlist:
    library.append(acquired)
    wishlist.remove(acquired)
print("\nUpdated Library: ", library)
print("Updated Wishlist: ", wishlist)
donate = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip: ")
if donate in library:
    library.remove(donate)
print("\nFinal Library after Donations: ", library)
