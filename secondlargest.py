
# Python program to find largest number in a list
 

list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
 
#to remove duplicate elements
list2 = list(set(list1))

list2.sort()
 

print("Second largest element is:", list2[-2])
