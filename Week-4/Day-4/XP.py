
# Ex-1
# def display_message():
#     print("Hi, I am learning python")
# display_message()

# Ex-2
# def favorite_book(title):
#     print(title + " is one of my favorite books")
# favorite_book("Alice in Wonderland")


# Ex-3

# def describe_city(city,country='Germany'):
#     print(city.title() + " is in " + country + '.')
#
# describe_city('Frankfurt')

# Ex-4
# import random
# mylist = []
#
# for i in range(1,100):
#     x = random.randint(1,10)
#     mylist.append(x)
# def compare_numbers(n):
#     if 0 < n < 100:
#         x = random.randint(0,100)
#         if n == x:
#             print("suceeded")
#         else:
#             print("failed")
# compare_numbers(10)

# Ex-5
# def make_shirt(size, message):
#     """Summarize the shirt that's going to be made."""
#     print("I am going to make a " + size + " t-shirt.")
#     print('It will say, "' + message + '"')
#
# make_shirt('large', 'I love Python!')
# make_shirt(message="shirts lovers.", size='medium')
#
# def make_shirt(size='large', message='I love Python!'):
#     """Summarize the shirt that's going to be made."""
#     print("\nI'm going to make a " + size + " t-shirt.")
#     print('It will say, "' + message + '"')
#
# make_shirt()
# make_shirt(size='medium')
# make_shirt('small', 'Perfect and fit.')

# Ex-6

# def show_magicians(magicians):
#     """Print the name of each magician in the list."""
#     for magician in magicians:
#         print(magician.title())
# magicians = ['David Copperfield', 'Doug Henning', 'Lance Burton']
# show_magicians(magicians)
#
# def make_great(magicians):
#
#     great_magicians = []
#     while magicians:
#         magician = magicians.pop()
#         great_magician = magician + ' the Great'
#         great_magicians.append(great_magician)
#
#     for great_magician in great_magicians:
#         magicians.append(great_magician)
#
# magicians = ['David Copperfield', 'Doug Henning', 'Lance Burton']
# show_magicians(magicians)
#
# make_great(magicians)
# show_magicians(magicians)


