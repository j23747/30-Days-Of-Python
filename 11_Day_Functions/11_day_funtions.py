#   defining a function

def trial():
    """
    This is a function that does nothing.
    """
    pass


## example of a funtion that adds two numbers

def addition():

    q = 10
    y = 20
    sum = q + y
    print(sum)

addition()


## example 2

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()


## example 3 returning a value

def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())


def subtract_two_numbers ():
    num_one = 18
    num_two = 5
    subtraction = num_one - num_two
    return subtraction

print(subtract_two_numbers())


## returning a list


def even_numbers(n):
    nos = []
    for i in range(n + 1):
        if i % 2 == 0:
            nos.append(i)
    return nos
print(even_numbers(20))
        


## calculating area of a circle

def area_of_circle(r):
    π = 3.14
    # r = 14
    return π * (r * r);
    # return area
print(area_of_circle(6))


## area of a triangle


def area_of_triangle(b, h):
    area = 0.5 * b * h
    return area


print(area_of_triangle(6, 2))