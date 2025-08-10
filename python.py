#Week 2 PLP Python Assignment:

#Create an empty list called my_list
my_list= []

#Append the following elements to my_list

my_list.extend([10,20,30,40])

#Insert the value 15 at the second position in list
my_list.insert(1,15)

#Extend my_list with another list
my_list.extend([50, 60, 70])

   #Remove 70 from the list
my_list.remove(70)


#Sort my_list in ascending order
my_list.sort(reverse=True)
print("Sorted list is:", my_list)

#Find and print the index of the value 30 in my_list
print("Index of 30:", my_list.index(30))
