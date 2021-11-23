# Ex-1

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# result = dict(zip(keys, values))
# print(result)

# Ex-2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# age = int(input("Enter age of enter '0' to quit:"))
# price = []
# active = True
# while age != 0:
#     age = int(input("Enter age or enter '0' to quit:"))
#     if age <= 3:
#         price.append(0)
#     elif age>3 and age<12:
#         price.append(10)
#     elif age== 0:
#         active = False
#     else:
#         price.append(15)
#     print(price)
# family_prices = zip(family.keys().price)
# prices = {}
# for i,j in family_prices:
#   prices(i) = j
#     print(family_prices)

# Ex-3
# brand = {'name': 'Zara',
# 'creation_date': 1975,
# 'creator_name': 'Amancio Ortega Gaona',
# 'type_of_clothes': ['men', 'women', 'children', 'home'],
# 'international_competitors': ['Gap', 'H&M', 'Benetton'],
# 'number_stores': 7000,
# 'major_color':{
#     'France': 'blue',
#     'Spain': 'red',
#     'US': ['pink', 'green']}}
#
# """ changing number of stores"""
# brand['number_stores'] = 2
#
# """Printing a message clients of Zara"""
# print("Men, women and children are Zaras client")
#
# """Adding a new key"""
# brand['country_creation'] = 'Spain'
#
# """checking if key is exist"""
# key="international_competitors"
#
# if key in brand.keys():
#     print("Key exists")
# else:
#     print("Key does not exist")
#
# """Adding a new value to key"""
# brand['international_competitors'].append('Desigual')
#
# """Deleting a key"""
# del brand['creation_date']
#
# """ Print the last international competitor"""
# print(brand['international_competitors'][3])
#
# """ Print the major clothes colors in the US."""
# print(brand['major_color']['US'])
#
# """ Print the amount of key value pairs"""
# for pair in brand.items():
#     print(pair)
#
# print("len() method :", len(brand))
# print("len() method with keys() :", len(brand.keys()))
# print("len() method with values():", len(brand.values()))
#
# """Print the keys of the dictionary."""
# print(brand.keys())
#
# """Creating a new dictionary"""
#
# more_on_zara = {'creation_date': 1975, 'number_stores': 10000}
# print(more_on_zara)


# Ex-4

# users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]
# disney_users_A = {}
# num = 0
# for i in users:
#    disney_users_A[i] = num
#    num += 1
#
# print(disney_users_A)
# disney_users_B = {value:key for key, value in disney_users_A.items()}
# print(disney_users_B)
# disney_users_C = dict(sorted(disney_users_A.items()))
# print(disney_users_C)
#
# users = [“Mickey”, “Minnie”, “Donald”,“Ariel”,“Pluto”]
# list_range_integers = list(range(len(users)))
# result_dict = {}
# for k, v in zip(users, list(range(len(users)))):
#     if ‘i’ in k and k[0] in [‘M’,‘P’]:
#         result_dict[k] = v
# for k, v in zip(list(range(len(users))), users):
#     result_dict[k] = v
# for k, v in zip(sorted(users), list(range(len(users)))):
#     result_dict[k] = v


# Ex-XP-Gold-1

# birthdays = {"John": "2000/03/14/","Eric": "1995/05/22","Leo": "1990/10/15",
#              "Tom": "1992/02/07", "Frank": "1994/12/26"}
#
# print("""Welcome to the birthday dictionary. You can look up the birthdays of the people in the list!
# John
# Eric
# Leo
# Tom
# Frank""")
#
# say = str(input("Who's birthday do you want to look up? : "))
#
# print(say, "Wishing you a very happy birthday!", birthdays[say])



# Timed Challange - 1

# Number = int(input(" Please Enter a Number: "))
# Sum = 0
# for i in range(1, Number):
#     if(Number % i == 0):
#         Sum = Sum + i
# if (Sum == Number):
#     print(True)
# else:
#     print(False)

