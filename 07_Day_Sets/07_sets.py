

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

## a set of kids names

kids = {'Emma', 'Noah', 'Olivia', 'Liam', 'Ava', 'Sophia', 'Mason', 'Isabella', 'Jacob', 'Mia', 'William'}

del kids
# print(kids)

## joining sets

st = {'item1', 'item2', 'item3', 'item4'}
kids = {'Emma', 'Noah', 'Olivia', 'Liam', 'Ava', 'Sophia', 'Mason', 'Isabella', 'Jacob', 'Mia', 'William'}

joined_set = st.union(kids)

print(joined_set)

## Difference between sets

st = {'item1', 'item2', 'item3', 'item4'}
kids = {'Emma', 'Noah', 'Olivia', 'Liam', 'Ava', 'Sophia', 'Mason', 'Isabella', 'Jacob', 'Mia', 'William'}
kids.difference(st)
st.difference(kids)

print(kids.difference(st))
print(st.difference(kids))

## example 2
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

print(whole_numbers.difference(even_numbers))

database_languages = {'SQL', 'Python', 'Java', 'C++', 'C#', 'JavaScript', 'PHP', 'C', 'Ruby'}
programming_languages = {'Python', 'Java', 'C++', 'C#', 'JavaScript', 'PHP', 'C', 'Ruby'}

## Example 3
database_languages.difference(programming_languages)
programming_languages.difference(database_languages)

print(database_languages.difference(programming_languages))



## Day 7 exercise

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}


## Find the length of the set it_companies

print(len(it_companies))

## Add 'Twitter' to the set it_companies
it_companies.add('Twitter')
print(len(it_companies))
print(it_companies)


## i nsert mutiple items to the set it_companies

it_companies.update (['Linkedin', 'Tesla', 'Glassdoor'])
print(it_companies)



## Remove 'Twitter' from the set it_companies

it_companies.remove('Twitter')
print(it_companies)


## remove multiple items from the set it_companies


it_companies.remove('Tesla')
it_companies.remove('Glassdoor')
it_companies.remove('Linkedin')
it_companies.remove('Amazon')

print(it_companies)

## use pop to remove a random item from the set it_companies

it_companies.pop()
print(it_companies)


## example 1

teachers = {'Mark', 'Susan', 'Anthony', 'Steve', 'Joe', 'John', 'David', 'Jennifer', 'Lisa', 'Nancy', 'Betty'}
print(teachers)
print(len(teachers))
print(teachers)
print(len(teachers))

teachers.discard('Mark')
print(teachers)
print(len(teachers))