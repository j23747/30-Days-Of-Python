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
