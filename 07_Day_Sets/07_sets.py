

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

## clearing items in a set
fruits.clear()
print(fruits)


### Deleting a Set

## If we want to delete the set itself we use _del_ operator.

## _del_ operator is used to delete a set. / fruits

st = {'item1', 'item2', 'item3', 'item4'}
del st



kids = {'Emma', 'Noah', 'Olivia', 'Liam', 'Ava', 'Sophia', 'Mason', 'Isabella', 'Jacob', 'Mia', 'William'}

del kids
# print(kids)
