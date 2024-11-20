""""Create an empty list called my_list.
Append the following elements to my_list: 10, 20, 30, 40.
Insert the value 15 at the second position in the list.
Extend my_list with another list: [50, 60, 70].
Remove the last element from my_list.
Sort my_list in ascending order.
Find and print the index of the value 30 in my_list."""

#Creating an empty List
my_list = list()
print(type(my_list)) #Confirming Type

#appending items into list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

#inserting 15 to the second position
my_list.insert(1, 15)
print(my_list)

#extending List
listb = [50,60,70]
my_list.extend(listb)

print(my_list)

#Deleting the Last element from My List
del my_list [7]
print(my_list)

#Sort List in ascending order
my_list.sort()
print(my_list)

#Find and print the index value 30
index = my_list.index(30)
print (index)
print(my_list[3])
