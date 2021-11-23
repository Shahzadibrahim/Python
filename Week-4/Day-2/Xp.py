# Ex-1

# my_fav_numbers = {3, 5, 7, 9, 19, 21}
# my_fav_numbers.update((25, 29))
# print(my_fav_numbers)
# my_fav_numbers.remove(25)
# print(my_fav_numbers)
# friend_fav_numbers = {14, 17, 28}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# Ex-2

# x_tuple = (5, 9, 13)
# No, you can't because tuples are immutable and therefore the sum can not be modified. You will have to create a new tuple.

# Ex-3

# for i in range(1, 21):
#    print(i)

# Ex-4

# Integers are numbers without a decimal point.
# float are numbers with decimal point.

# my_list = 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
# print(my_list)

# Ex-5

# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# new_fruit = "Apples"
# basket.insert(0, new_fruit)
# fruit_count = basket.count("Apples")
# basket.clear()
# print(basket)


# Ex-6

# keep_going = True
# while keep_going:
#     name = input('Enter correct name, or type quit to exit ')
#     if name == "shahzad":
#        keep_going = False

# Ex-7

# list1 = [10, 21, 4, 45, 66, 93, 8, 13, 25, 12, 34, 37]

# for num in list1:
#    if num % 2 == 0:
#        print(num)

# Ex-8

# for i in range(1500,2500):

#    if i%7==0 and i%5==0:

#        print(i)

# Ex-9

# fruit = input("What is your favourite fruit? ")
# fruit = list(fruit)
# for i in fruit:
#    print(i)

# Ex-10

# prompt = "\nWhat topping would you like on your pizza?"
# prompt += "\nEnter 'quit' when you are finished: "

# while True:
#    topping = input(prompt)
#    if topping != 'quit':
#        print("  I'll add " + topping + " to your pizza.")
#    else:
#        break

# Ex-11

# prompt = "How old are you?"
# prompt += "\nEnter 'quit' when you are finished. "
#
# while True:
#    age = input(prompt)
#    if age == 'quit':
#        break
#    age = int(age)
#
#    if age < 3:
#        print("  You get in free!")
#    elif age < 13:
#        print("  Your ticket is $10.")
#    else:
#        print("  Your ticket is $15.")


# Ex-13

# sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
# finished_sandwiches = []

# while sandwich_orders:
#    current_sandwich = sandwich_orders.pop()
#    print("I'm working on your " + current_sandwich + " sandwich.")
#    finished_sandwiches.append(current_sandwich)

# print("\n")
# for sandwich in finished_sandwiches:
#    print("I made a " + sandwich + " sandwich.")

# Ex-14

# sandwich_orders = [
#    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
#    'turkey', 'roast beef', 'pastrami']
# finished_sandwiches = []

# print("I'm sorry, we're all out of pastrami today.")
# while 'pastrami' in sandwich_orders:
#    sandwich_orders.remove('pastrami')

# print("\n")
# while sandwich_orders:
#    current_sandwich = sandwich_orders.pop()
#    print("I'm working on your " + current_sandwich + " sandwich.")
#    finished_sandwiches.append(current_sandwich)

# print("\n")
# for sandwich in finished_sandwiches:
#    print("I made a " + sandwich + " sandwich.")


