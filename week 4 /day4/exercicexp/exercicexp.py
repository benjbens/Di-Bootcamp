

# Exercice 1



# def display_message():
#     print("python")

# display_message()    


# Exercice 2 




# def favorite_book(title):
#     print(f"One of my favorite books is {title}")


# favorite_book("1984")


# Exercice 3 

# city = "paris"
# country = "france"

# def describe_city():
#     print(f"{city} is in {country}")

# describe_city()

# Exercice 4 


# def randome_numbers():
#     user = int(input ("guess a number from 1 to 100: "))
#     print(user)
#     randome = (randint(1, 100))
#     print(randome)

#     if randome == user:
#         print("good")

#     else:
#         print("fail")


# randome_numbers()


# Exercice 5 

# def make_shirt():
#     print("the t shirt is in L")
#     size = int(input("what's your size"))
#     message = input("print a message: ")
#     print(f"the message is {message} and my size is {size}")



# make_shirt()

# Exercice 6 

# magiciens = ["fernando", "Jojo", "Jackie"]

# def show_magicians(magiciens):
    
#     for i in magiciens:
#         print(i)

# show_magicians(magiciens)



# def make_great(magiciens):

#  new_list = ["the great " + i for i in magiciens]
#  print(new_list)


# make_great(magiciens)


matrix = [['7', 'i', '3'],
          ['T','s','i'],
          ['h','%','x'],
          ['i',' ','#'],
          ['s','M',' '],
          ['$','a',' '],
          ['#','t','%'],
          ['^','r','!']]
result = ""
#len(matrix[0]) -> 3
special_chars = 0
for column in range(len(matrix[0])):
    #len(matrix) -> 8
    for row in range(len(matrix)):
        print(matrix[row][column])

        if matrix[row][column].isalpha():
            result += matrix[row][column] 
            special_chars = 0

        else:
            if special_chars == 2 or matrix[row][column] == " ":
                result += " "
            else: 
                special_chars += 1




print(result)
































