# Set
# Definition: Set is a collection of objects.
# Syntax: <variable_name> = {<object_1>, <object_2>, ...}
set_of_os = {"Windows", "Mac OS", "Linux", "Unix", "Windows", "Linux"}
print(set_of_os)
print(type(set_of_os))

# Properties of a Set:
# 1) The objects inside a set does not have an index (location)
# 2) Duplicates are not allowed in sets

# Objective: remove duplicates from the following list without any iteration:
list_of_duplicate_items = ["Windows", "Windows", "Windows", "Unix", "Unix"]
set_of_items = set(list_of_duplicate_items)
list_of_unique_items = list(set_of_items)
print(list_of_unique_items)

# Objective: find the common items between two lists
list_1 = ["a", "b", "c"]
list_2 = ["b", "c", "d", "e"]
converted_set_1 = set(list_1)
converted_set_2 = set(list_2)
common_items = converted_set_1.intersection(converted_set_2)
items_in2_notin1 = converted_set_2.difference(converted_set_1)
items_in1_notin2 = converted_set_1.difference(converted_set_2)
sum_of_items = converted_set_1.union(converted_set_2)
print(common_items)
print(items_in2_notin1)
print(items_in1_notin2)
print(sum_of_items)