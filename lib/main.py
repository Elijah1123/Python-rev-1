# # print("I like pizza1")
# # print("It's really good!")

# # Variable = A container for a value  (string, integer, float, boolean
# #            Avariable behaves as if it was the value it contains    

# # Below are Strings
# # As String is a serious of characters 
# first_name = "Mzalendo"
# food = "pizza"
# email = "mzalendo659@gmail.com"

# print(f"Hello {first_name}")
# print(f"You like {food}")
# print(f"Your email is: {email}")

 
# #Integers

# age = 22
# quantity = 3
# num_of_student = 30

# print(f'You are {age} years')
# print(f'You are buying {quantity} items')
# print(f'Your class has {num_of_student} students')


# # Float

# price  = 10.99
# gpa =   3.5
# distance = 6.45

# print(f"The price is ${price}")
# print(f"Your gpa is {gpa}")
# print(f"Your run {distance} km")

# # Boolean

# is_student = False
# if is_student: 
#     print(f"You are a  student")
# else:
#     print("You are NOT a student")

# for_sale = True
# if for_sale:
#     print("That Item is for sale")
# else:
#     print("That item is not available")    

# is_online = True
# if is_online:
#     print("You are online")
# else:
#     print("You are offline")    

# is_learning = True
# if is_learning:
#     print("You are learnimg")
# else:
#     print("You are Not Learning")

# #Typecasting = the process of  converting a variable from one data type to another
# #              str(), int(), float(), bool()

# name = "Elijah Mzalendo"
# age  = 22
# gpa = 4.5
# is_student = True

# gpa = int(gpa)
# age = str(age)

# age += "1"

# print(age)
# print(gpa)


# print(type(name))
# print(type(age))
# print(type(is_student))


#input() = A function that prompts user to enter data  
#          Returns the entered data as a string   

# name = input("What is your name? ")
# age  = input("How old are you?")

# age = int(age)
# age = age + 1

# print(f"Hello {name}")
# print("HAPPY BIRTHDAY!")
# print(f"You are now {age} years old")


#Exercise 1 Rectangle Area Calculator

# length = input("Enter rectangle length: ")
# width = input("Enter rectangle width: ")

# length = float(length)
# width = float(width)
# area = length * width
# print(f"The area of the rectangle is {area} square units.")

# Exercise 2 Shopping Cart Program

# item_1 = input("Enter the price of item 1: ")
# item_2 = input("Enter the price of item 2: ")

# item_1 = float(item_1)
# item_2 = float(item_2)

# total = item_1 + item_2
# print (f"The total price of item 1 and item 2 is: Ksh {total:}")

# item = input("What item would you like to buy?: ")
# price = input("What is the price of the item?: ")
# quantity = input("How many items would you like to buy?: ")
# total = float(price) * int(quantity)

# print(f"You are buying {quantity} {item}(s) at a price of Ksh {price} each.")
# print(f"The total price is Ksh {total:.2f}")

#Madlibs game
# word game where you create a story
# by filling in blanks with words

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, or thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with  -ing: ")
adjective3 = input("Enter an adjective (description): ")

print(f"Today I went to a {adjective} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}! ")
