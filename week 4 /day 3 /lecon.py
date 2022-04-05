# available_sandwiches = ["Tuna", "Salmon", "Vegetarian"]
# available_sandwiches += ['pastrami'] * 3
# finished_sandwiches = []

# while 'pastrami' in available_sandwiches:

#     available_sandwiches.remove('pastrami')



# while len(available_sandwiches) > 0:

#     finished_sandwiches.append(available_sandwiches.pop(0))

#     print(f"I have just finished your {finished_sandwiches[-1]} sandwich")



# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# print(sample_dict["class"]["student"]["marks"]["history"])




# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# del sample_dict["name"]
# del sample_dict["salary"]

# print (sample_dict)

some_string ="hello world"

a_list = [some_string[:i] for i in range(1, len(some_string)+1)]
print(a_list)