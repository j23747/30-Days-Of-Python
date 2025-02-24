## String methods

## 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

full_string = 'Thirty' + ' Days' + ' Of' + ' Python'

print(full_string)


## 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

coding_for_all = 'Coding' + ' For' + ' All'

print(coding_for_all)

## 3. Declare a variable named company and assign it to an initial value "Coding For All".
var_company = 'Coding For All'

print(var_company)


print(var_company.swapcase())

## 7.Change all the characters to lowercase letters using _lower()_ method.

print(var_company.lower())


## 8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.

print(var_company.capitalize())
print(var_company.title())
print(var_company.swapcase())


## 9. Cut(slice) out the first word of _Coding For All_ string.

print(var_company.split()[1])

## 10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.   

var_company = 'Coding For All'

print(var_company.find('Coding'))
print(var_company.index('Coding'))


## Another example string.index(substring, start, end)

my_string = "Where's Waldo?"
print(my_string.find("Waldo", 0, 6))


## 11. Replace the word coding in the string 'Coding For All' to Python.

var_company = 'Coding For All'

var_replaced_string = var_company.replace('Coding', 'Python')

print(var_replaced_string)

## Another example

var_full_names = 'Josphat Mwania'

var_new_name = var_full_names.replace('Josphat', 'Phatjay')
print(var_new_name)

## 12. Change Python for Everyone to Python for All using the replace method or other methods.

var_python_for_everyone = 'Python for Everyone'
var_python_for_all = var_python_for_everyone.replace('Everyone', 'All')
print(var_python_for_all)