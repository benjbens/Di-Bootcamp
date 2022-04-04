# Exercice 1 

# my_fav_numbers = {1, 2, 3}


# my_fav_numbers =  my_fav_numbers | {4,5}


# my_fav_numbers.remove(5)



# friend_fav_numbers = {6, 7, 8}


# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)



# Exercice 2

# no

# Exercice 3 

#   print(x)


# Exercie 4 

# integers are numbers without a decimal point, whereas floats are numbers with a decimal point.




# for j in range(1, 6):
#     print(j-0.5)
#     print(j)

# list = [j]


# Exercice 5 

# basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# basket.remove("Banana")


# basket.remove("Blueberries")


# basket.append("Kiwi") 


# basket.insert(0, "Apples")

# print(basket.count("Apples"))

# basket.clear()
# print(basket)

# Exercice 6

   

# name = ""

# while name != "benji":
#     name = input("Name: ")

#     loops = 0 

# Exercice 7 


# for i in range(11):
#   if i % 2 == 0:
#     print(i)

# Exercice 8 

# for i in range(1500, 2500):
#     if (i % 5==0):
#         if (i % 7==0):
#             print(i)

# Exercice 9

# fruit = input("your favorit fruit: ")
# print(fruit)

# list = fruit.split()
# print(list)

# fav_fruit =input("input a name of any fruit: ")

# if fav_fruit in fruit:
#     print("You chose one of your favorite fruits! Enjoy!”")

# else:
#     print("You chose a new fruit. I hope you enjoy”")

    # Exercice 10

# prices = 10 

# while True:
#         print("Loop number:", prices)
#         user = input("Q: Quit; M:mushrooms; O:Olive ")

#         if user == "Q":
#             print("Exiting loop...")
#             break

#         elif user == "M":
#             print("Mushrooms")
            
#         elif user == "O":
#             print("Olive")

#         else:
#             continue

#         prices += 2.5

# print(prices)

# Exercice 11 

# user =  int(input("How old are u ?: "))
    
#         if user < 3:
#             print("the ticket is free")
#         if user >= 3 and user <= 12:
#             print("the ticket is $10")
#         if user > 12:
#             print("the ticket is $15.")



# Exercice 12

from os import remove


names = ["Adam", "Ben", "David", "Meiron"]

for name in names:
    age = int(input(f"{name}, what's your age?: "))
    if age < 16:
        names.remove()
        print(names)
        



