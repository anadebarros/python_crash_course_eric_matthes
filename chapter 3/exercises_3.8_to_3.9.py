# 3.8
places = ["canada", "seattle", "alaska", "north pole", "china"]

print(places)

# store list into a variable. I could do print(sorted(places)) instead
in_order = sorted(places)
print(in_order)

# show that original list was not modified
print(places)

# reverse the list alphabetically without changing the order of original list
print(sorted(places, reverse=True))

# show that original list was not modified
print(places)

# permanently change the order of the list
places.reverse()

print(places)

# reverse the order of the list again
places.reverse()

print(places)

# permanently sort the list in alphabetical order
places.sort()

print(places)

# permanently reverse the list in alphabetical order
places.sort(reverse=True)

print(places)

# 3.9
invitees = ["kurt cobain", "jeff buckley", "dylan reider"]
print(f"Hey guys, I'm inviting {len(invitees)} people for dinner tonight!")

# I did not go through exercise 3.10 as it is basically jsut going through all previous exercises in the chapter
