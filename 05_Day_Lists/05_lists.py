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