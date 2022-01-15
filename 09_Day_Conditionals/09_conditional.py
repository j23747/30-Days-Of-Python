
# conditions using if, elif, else


def main():
    if 1 == 1:
        print("1 is equal to 1")
    elif 2 == 2:
        print("2 is equal to 2")
    else:
        print("1 and 2 are not equal")


## example of a function that returns a value



value = int(input("Enter a number: "))

if value == 30:
    print("You entered 30")
elif value == 40:
    print("You entered 40")
else:
    print("You did not enter 30 or 40")


## example 2

user = 'Josphat'

access_level = 'student'
if user == 'Josphat':
    if access_level == 'student':
        print("You have access to the student portal")
    elif access_level == 'teacher':
        print("You have access to the teacher portal")
    else:
        print("You have no access")
else:
    print("You are not authorized")



user = 'Mike'
access_level = 'teacher'
if user == 'Josphat':
    print("You have access to the student portal")
elif access_level == 'teacher':
    print("You have access to the teacher portal")


age = input("Enter your age:...")

if age >= '18':
    print("You are old enough to drive")
elif age < '18':
    print("You need more years to learn to drive")
