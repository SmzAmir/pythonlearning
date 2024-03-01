# List
# Definition: List is a collection of objects.
# Syntax: <variable_name> = [<object_1>, <object_2>, ...]
list_of_os = ["Windows", "Mac OS", "Linux", "Unix", "Windows", "Linux"]
print(list_of_os)
print(type(list_of_os))

# Properties of a List:
# 1) The objects inside a list is indexed (location)
# 2) The list is mutable (you can alter the objects of a list)
# 3) Duplicates are allowed in lists

# Extract objects by an index
# <variable_name>[<index>]
# <index> is a whole number (a number without a decimal point)
# <index> in Python starts from 0 by default
print(list_of_os[0])
print(list_of_os[1])
print(list_of_os[2])
print(list_of_os[3])
print(list_of_os[4])

# What is the range of numbers that I pass as an index?
length_of_list_os = len(list_of_os)
print(length_of_list_os)
max_index = length_of_list_os - 1
print(max_index)

# nested lists means lists within lists
nested_list = [0, 9, 8, [2, 5, [-4, 7], 3, 0], 6]
# How to get -4? By chaining the index
print(nested_list[3])
print(nested_list[3][2])
print(nested_list[3][2][0])
print(nested_list[3][2][0])

list_of_os_new = ["Windows", "Mac OS", "Linux", "Unix"]

# Extract a range of objects by an index
# <variable_name>[<start_index>:<end_index>:<step_size>]
# Note: The object of <end_index> will not be included in the search
# Note: <step_size> is by default 1
print(list_of_os_new[0:2])
print(list_of_os_new[0:2:1])
print(list_of_os_new[-1:-3:-1])
print(list_of_os_new[-3:-1])

# Functions or methods of a list (altering a list):
# 1) <list_variable>.append(<object>): adds item to the end of a list
# print(list_of_os_new)
list_of_os_new.append("Windows")
print(list_of_os_new)

# 2) <list_variable>.remove(<object>): removes item from a list
list_of_os_new.remove("Windows")
print(list_of_os_new)

# 3) <list_variable>.pop(<index>): removes item from a list using an index
list_of_os_new.pop(1)
print(list_of_os_new)

# 4) <list_variable>.insert(<index>, <object>): adds an item using the index and a value
list_of_os_new.insert(2, "Mac OS")
list_of_os_new.insert(2, "Windows")
print(list_of_os_new)

# 5) <list_variable>.count(<object>): counts the number of appearance of an object
print(list_of_os_new.count("Windows"))
print(list_of_os_new.count("Mac OS"))
print(list_of_os_new.count("Unix"))












