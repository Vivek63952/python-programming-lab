# Python program to find sum of elements in list
total = 0
i= 0
 

list1 = [11, 5, 17, 18, 23, 56, 87]
 

while(i < len(list1)):
    total = total + list1[i]
    i += 1
     
print("Sum of all elements in given list: ", total)
