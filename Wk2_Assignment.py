#Empty list called my_list
my_list = []
print(my_list)  # Output: []

#appedning elements to my_list
my_list.extend([10, 20, 30, 40])
print(my_list)  # Output: [10, 20, 30, 40

#inserting a value in the second position
my_list.insert(1, 15 )
print(my_list)  # Output: [10, 15, 20, 30, 40]

#Extending my_list with another list
my_list.extend([50, 60, 70])
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60, 70]

#removing the last element
my_list.pop()
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]

#sorting my_list in asc order
my_list.sort()
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]

# Finding the index of a value
Index_of_value_30=my_list.index(30) 
print("Index of value 30:", Index_of_value_30)  # Output: Index of value 30: 3