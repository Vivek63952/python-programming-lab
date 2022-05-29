# Python3 Program to find sum of all items in a Dictionary 
  
def returnSum(dict):
 
    sum = 0
    for i in dict.values():
        sum = sum + i
 
    return sum
 
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))
