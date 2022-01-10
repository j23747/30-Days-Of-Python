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

print(developer_01['Stacks'])
print(developer_01['full_address'])