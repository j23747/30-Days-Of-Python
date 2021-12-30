## creating an empty list
empytList = list()

print(len(empytList))


## List of siblings

siblings = ['Howard', 'Joseph', 'Richard', 'Geoffrey', 'Charles']

print('siblings Are:', siblings)

## ACcesiong the fist sibling

first_sibling = siblings[0]
print(first_sibling)

## Accessing the last sibling index 

last_index = len(siblings) - 1
print(last_index)

# Checking items

does_exist = 'Charles' in siblings
does_exist = 'Richardd' in siblings
print(does_exist)



# Append (adding an item to the end of the list)

siblings.append('Cvavy')
print(siblings)


## insert (adding an item to the list at a specific index)

siblings.insert(4, 'Grace')

print(siblings)

## insert 
siblings.insert(2, 'Susan')
print(siblings)

## remove (removing an item from the list)

siblings.remove('Susan')
print(siblings)

## pop (removing an item from the list)

siblings.pop()
print(siblings)

## pop 
siblings.pop(0)

# deleting an item in a list

del siblings[0]
print(siblings)


##  Finding the index of an item

programming_languages = ['Python', 'Java', 'C++', 'C#', 'JavaScript']

programming_languages.index('Java')

print(programming_languages.index('Java'))


## Reverse a list

programming_languages = ['Python', 'Java', 'C++', 'C#', 'JavaScript']

programming_languages.reverse()
print(programming_languages)


## Sort a list


programming_languages = ['Python', 'Java', 'C++', 'C#', 'JavaScript']
programming_languages.sort()  # ascending   alphabetical order
print(programming_languages)


programming_languages.sort(reverse=True)  # descending  alphabetical order
print(programming_languages)

## example 2
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending
print(lst)

## Join the following lists

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

Join_lists = front_end + back_end
print(Join_lists)

## After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

insert_python_sql = Join_lists.copy()
insert_python_sql.insert(5, 'Python')
insert_python_sql.insert(6, 'SQL')
print(insert_python_sql)


### Exercises: Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

ages.sort(reverse=True)
print(ages)