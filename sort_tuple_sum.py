
# Python code to sort list of tuple based on sum of element in tuple.
  
input = [(4, 5), (2, 3), (6, 7), (2, 8)] 
  
print("The original list of tuple is ")
print(input)
  

lst = len(input)
  
for i in range(lst):
      
    for j in range(lst-i-1):
        if (input[j][0]+input[j][1]) > (input[j+1][0]+input[j+1][1]):
            input[j], input[j+1] = input[j+1], input[j]
  
 
print("\nThe answer is")
print(input)
