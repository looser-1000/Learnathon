print("Welcome back to Python, Humayra")

# variable
patient_name = "John Mash"
print(patient_name, "is our new patient")

# receive input
name = input("What is your name? ")
print("Welcome,"+ name)

# Type Conversion
birth_year = input("Type Your Birth Year: ")
current_age = 2024 - int(birth_year)
print(name + ", your Current Age is : " ,current_age)

#  all build in function in Python are
# int()
# float()
# bool()
# str()
#

first_num = input("Type an integer number: ")
second_num = input("Type a floating point number: ")
sum = int(first_num) + float(second_num)
print("The Sum value is: ", sum)


# string
course = "Python learning Course for beginner"
print(course.upper())
print(course.lower())
print(course.find('P'))
print(course.replace('for', '4'))
print('Python' in course)


# IF statement
tem = -10
if tem > 30 :
    print("It is a hot day")
elif tem > 25:
    print("It is a  nice day")
elif tem > 20:
    print("It's bit cold today")
elif tem > 0:
    print("It's Freezing today")
else:
    print("It's Snowing")


weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    changed = weight / .45
    print("Weight in Lbs: " + str(changed))
else :
    changed = weight * .45
    print("Weight in Kg: " + str(changed))


numbers = [40, 50, 70, 100]
for item in numbers:
    print(item)


i = 1
while i <= 10:
    print(i * '*')
    i = i + 1


# List
name = ["Lily", "Puti", "Dimple", "Daisy", "Lotus"]
print(name[0:3])  #only first three element of the array will be shown
print(name[-1])  #last element of the array will be shown

# List Method
number = [1, 2, 3, 4, 5]
number.append(6)
print(number)
number.insert(2, 7)
print(number)
number.remove(3)
print(number)
# number.clear() it is used to delete all the elements of the array


# Range
items = range(5, 10, 2)
for item in items:
    print(item)

num = [10, 5, 60, 80, 100]
i = 0
while i < len(num):
    print(num[i])
    i = i+1


