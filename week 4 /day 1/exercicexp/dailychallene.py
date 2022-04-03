import random

user = input("Please enter a string:")
lenghtuser = len(user)

if lenghtuser  < 10:
    print("string not long enough")
elif lenghtuser > 10:
    print("string too long")
else:
    print ("okey")

last_char = user[-1]
print('Last character : ', last_char)

first_char = user[0]
print('First character:',first_char)

empty = ""
for letter in user:
    empty = empty + letter
    print(empty)


arr = list(user)
print(user)

random.shuffle(arr)
print(arr)



  