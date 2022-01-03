

## Empty set {}

set_01 = set()

set_1 = {1, 2, 3, 4, 5}

## finiding length of set

len(set_1)
print(set_1)
print(len(set_1))



## Adding and item in a set
set_1.add(6)

print(set_1)


## Removing an item from a set

set_1.remove(1)

print(set_1)

## using pop method
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
print(fruits)

## knowing the removed item/fruit
removed_fruit = fruits.pop()
print(fruits)

