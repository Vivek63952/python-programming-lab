# Python program to create a list of tuples from given list having number and its cube in each tuple
  
list1 = [1, 2, 5, 6]
  
res = [(val, pow(val, 3)) for val in list1]
  

print(res)
