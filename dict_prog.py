
# Python code to demonstrate combining two dictionaries having same key
 

ini_dict1 = {'nikhil': 1, 'akash' : 5, 'manjeet' : 10, 'akshat' : 15}
ini_dict2 = {'akash' : 7, 'akshat' : 5, 'm' : 15}
  
print ("initial 1st dictionary", str(ini_dict1))
print ("initial 2nd dictionary", str(ini_dict2))
  
# combining dictionaries

final_dictionary =  {x: ini_dict1.get(x, 0) + ini_dict2.get(x, 0)
                    for x in set(ini_dict1).union(ini_dict2)}

print ("final dictionary", str(final_dictionary))
