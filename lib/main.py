# print("I like pizza1")
# print("It's really good!")

# Variable = A container for a value  (string, integer, float, boolean
#            Avariable behaves as if it was the value it contains    

# Below are Strings
# As String is a serious of characters 
first_name = "Mzalendo"
food = "pizza"
email = "mzalendo659@gmail.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")


#Integers

age = 22
quantity = 3
num_of_student = 30

print(f'You are {age} years')
print(f'You are buying {quantity} items')
print(f'Your class has {num_of_student} students')


# Float

price  = 10.99
gpa =   3.5
distance = 6.45

print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"Your run {distance} km")

# Boolean

is_student = False
if is_student: 
    print(f"You are a  student")
else:
    print("You are NOT a student")

for_sale = True
if for_sale:
    print("That Item is for sale")
else:
    print("That item is not available")    

is_online = True
if is_online:
    print("You are online")
else:
    print("You are offline")    

is_learning = True
if is_learning:
    print("You are learnimg")
else:
    print("You are Not Learning")

#Typecasting = the process of  converting a variable from one data type to another
#              str(), int(), float(), bool()

name = "Elijah Mzalendo"
age  = 22
gpa = 4.5
is_student = True

gpa = int(gpa)
age = float(age)

print(age)
print(gpa)


print(type(name))
print(type(age))
print(type(is_student))
  