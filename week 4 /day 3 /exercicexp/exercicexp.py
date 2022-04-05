# Exercice 1 

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# result = dict(zip(keys, values))
# print(result)

# Exercice 3

# brand = {
#     "name": "Zara",
#     "creation_date": "1975",
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ['men', 'women', 'children', 'home'],
#     "international_competitors": ['Gap', 'H&M', 'Benetton'],
#     "number_stores": 7000,
#     "major_color": {
#         "France": "blue", 
#         "Spain": "red",
#         "US": ["pink, green"]
#     }
# }

# brand["number_stores"] = 2


# # print("Zaras clients are", brand["type_of_clothes"])

# brand["country_creation"] = "Spain"


# brand["international_competitors"] ="desigual"


# del brand["creation_date"]


# print(brand["international_competitors"][-1])

# print(brand["major_color"]["US"])

# print(len(brand))

# print(brand.keys())

# more_on_zara = {

#     "creation_date": 1975,
#     "number_stores": 10000,
# }

# brand.update(more_on_zara)
# print(brand)

# print(brand["number_stores"])


# Exercice 4

# disney_users_A = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# print({name: disney_users_A.index(name) for name in disney_users_A})

# disney_users_B = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# print({disney_users_A.index(name):name for name in disney_users_A})



# disney_users_A = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# disney_users_A = sorted(disney_users_A)
# print({name: disney_users_A.index(name) for name in disney_users_A})

disney_users_A = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# print({name: disney_users_A.index(name) for name in disney_users_A})

# empty_list = [ ] 
# for carachtere in disney_users_A:
#     if carachtere.count("i") != 0:
#         empty_list.append(carachtere)
        
        
    
# print({name: empty_list.index(name) for name in empty_list})
    
    
empty_list = []

empty_list = [ ] 
for carachtere in disney_users_A:
    if carachtere[0] == "M" or carachtere[0] == "P":
        empty_list.append(carachtere)


print({name: empty_list.index(name) for name in empty_list})