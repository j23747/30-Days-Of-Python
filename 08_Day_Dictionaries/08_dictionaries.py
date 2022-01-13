## Dictionaries definition

## A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.



## empty dictionary

# dict_empty = {}


# dict_siblings_data = {'Name': 'Fred', 'Age': '25', 'Occupation': 'Engineer' }


# print(dict_siblings_data)

# example with many data type

developer_01 = {
    'First_name': 'Abdul',
    'last_name': 'Moha',
    'residence': 'Garissa',
    'Position': 'Senior Developer',
    'Stacks':['Android', 'Spring Boot', 'Ract', 'Java'],
    'full_address': {
        'street': 'Eastleigh',
        'postal_code': '00200'
    }
}
## Accessing items from the dictionary
print(developer_01['Stacks'])
print(developer_01['full_address'])

## Using the get method to access items by key name

print(developer_01.get('First_name'))
print('Is the first name' in developer_01.get('First_name'))


## Adding items to the dictionary

developer_01['Age'] = '30'
developer_01['Salary'] = 'Kes100,000'

print(developer_01.get('Age'))
print(developer_01.get('Salary'))

## add more items to the dictionary

developer_01['Department'] = 'IT'
developer_01['Nature_of_employment'] = 'Full Time'

print(developer_01.get('Department'))
print(developer_01.get('Nature_of_employment'))

## Changing items in the dictionary/modifyng items in the dictionary

developer_01['residence'] = 'Nairobi'
developer_01['Position'] = 'Senior Android Developer'

print(developer_01.get('residence'))
print(developer_01.get('Position'))

developer_01.pop('full_address')

print(developer_01.get('full_address'))


## clearing a dict

print(developer_01.clear())

## deleting a dict completely

del developer_01


## copying a dict

# example 1
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

print(dct_copy)


## example 2

siblings_dict = {'Name': 'Fred', 'Age': '25', 'Occupation': 'Engineer' }

copy_siblings_dict = siblings_dict.copy()

print(copy_siblings_dict)

## get dict keys as a list use _keys()

keys = siblings_dict.keys()
print(keys)


dog = {}

dog = {'Name':'Lucky', 'Color':'black', 'Breed': 'Germany Shepherd', 'legs':'tall', 'age': '5' } 
print(dog)
print(dog.get('Name'))