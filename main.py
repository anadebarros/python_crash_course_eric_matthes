
#7.5
prompt = "Hi, what is your age? "

while True:
  message = input(prompt)
  if int(message) <=3:
    print("Your entry is free!")
  elif int(message) <=12:
    print("Your ticket is 10$")    
  else:
    print("Your ticket is 15$")
  break

#7.6
prompt = "Hi, what is your age? "
value = True

while value:
  message = input(prompt)
  if int(message) <=3:
    print("Your entry is free!")
    value = False  
  else:
    print("You'll need money!")
    value = False
