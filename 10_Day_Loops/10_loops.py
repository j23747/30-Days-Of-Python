# ## 1. while loop & 2. for loop

# # example 1

# count = 0
# while count < 3:
#     print(count)
#     count = count ++1

# print('Example 1 is done')
# ## example 2

# number = 0

# while number < 5:
#     print(number)
#     number = number +1

# # print('Results for example 2')

# ## Example 3 with else condition

# # number = 0

# # while number < 5:
# #     print(number)
# #     number == number +1
# # else:
# #    print(number)


# ### using continue

# # example 


# # ```py
# # while condition:
# #     code
# #     if another condition:

# #         continue

# # ```py

# ## example 4

# counts = 0
# while count < 5:
#     if counts == 3:
#         continue
#         print(counts)



## Using For loop in  a list

randoms = [0, 1, 2, 3, 4]

for random in randoms :
    # print('Here is for loops')
    print(random) 


## example 5

language = 'Java'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])
