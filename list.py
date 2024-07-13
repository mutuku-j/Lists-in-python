my_list=[]

#Appending the elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting the value 15 at the second position
my_list.insert(1, 15)

#Extending my_list with another list
my_list.extend([50, 60, 70])

#Removing the last element
my_list.pop()

#Sorting my_list in ascending
my_list.sort()
print(my_list)

#Finding and printing the index of the value 30
index_of_30=my_list.index(30)
print('Index of 30 is:',index_of_30)