# 3.4
invitees = ["kurt cobain", "jeff buckley", "dylan reider"]

message1 = "Hi, I would like to invite " + invitees[0].title() + " to dinner!"
message2 = "Hi, I would like to invite " + invitees[1].title() + " to dinner!"
message3 = "Hi, I would like to invite " + invitees[2].title() + " to dinner!"

print(message1, message2, message3)

# 3.5
print(f"Unfortunately, {invitees[1].title()} will not be able to join us :(")

invitees[1] = "philipp s. hoffman"

message1 = "Hi, I would like to invite " + invitees[0].title() + " to dinner!"
message2 = "Hi, I would like to invite " + invitees[1].title() + " to dinner!"
message3 = "Hi, I would like to invite " + invitees[2].title() + " to dinner!"

print(message1, message2, message3)

# 3.6
print(f"{invitees[0].title()}, {invitees[1].title()}, {invitees[2].title()}: I have found a bigger dinner table!")

invitees.insert(0, "aimee winehouse")
invitees.insert(1, "jim morisson")
invitees.append("dakar")

for i in invitees:
    print(f"I would like to invite {i.title()} to this amazing dinner!")

# 3.7

for i in invitees:
    print(f"Oppsies {i.title()} I can only invite two people for dinner :/")

guest1 = invitees.pop()
print(f"I'm sorry {guest1.title()}, I can't invite you for dinner")

guest2 = invitees.pop()
print(f"I'm sorry {guest2.title()}, I can't invite you for dinner")

guest3 = invitees.pop()
print(f"I'm sorry {guest3.title()}, I can't invite you for dinner")

guest4 = invitees.pop()
print(f"I'm sorry {guest4.title()}, I can't invite you for dinner")

for i in invitees:
    print(f"Hey {i.title()} you are still invited!")

del invitees[1]
del invitees[0]

print(invitees)
