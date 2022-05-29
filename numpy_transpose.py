#PROGRAM TO GET TRANSPOSE OF A MATRIX USING NUMPY
import numpy as np
 
trans = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
 
print("before transpose")  
print(trans, end ='\n\n')
 
print("after transpose")
print(trans.transpose())
