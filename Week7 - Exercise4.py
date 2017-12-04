shoplist = []

add = input("Would you like to add something to your shopping list? Y or N?")

while add.lower() == "y":
    item = input ("Enter your item to the list:")
    shoplist.append(item)
    add = input("Would you like to add something your shopping list? Y or N?")

print()
print("Here is your shopping list in alphabetical order.")
shoplist.sort()
for listitem in shoplist:
    print(listitem)
