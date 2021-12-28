### ethods related to tuples:

## - tuple(): to create an empty tuple
## - count(): to count the number of a specified item in a tuple
## - index(): to find the index of a specified item in a tuple
## - + operator: to join two or more tuples and to create a new tuple
## - * operator: to repeat a tuple a specified number of times

##  empty tuple()
tup1 = ()
empty_tuple = tuple()
print(empty_tuple)

## tuple with one item

tuple_1 = ('item1')
print(tuple_1)

tuple_2 = ('item1', 'item2', 'item0')
print(tuple_2)

## length of a tuple

len(tuple_2)
print(tuple_2)

tpl = ('item1', 'item2', 'item3')
len(tpl)
print(tpl)

### Accessing Tuple Items

tuple_students = ('Eric', 'Josphat', 'Clare', 'Nick', 'Sophie', 'Abdul')
first_student = tuple_students[0]
print(first_student)

## accessing index 5 item
fifth_student = tuple_students[4]
print(fifth_student)
# print(tuple_students)

## Example 2

fruits = ('banana', 'orange', 'mango', 'Melon', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]
print(first_fruit)
print(second_fruit)
print(last_fruit)

## second last item

second_last_index = len(fruits) - 2 # negative indexing
second_last_fruit = fruits[second_last_index]
print(second_last_fruit)
