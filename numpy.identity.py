#PROGRAM TO GET IDENTITY MATRIX
import numpy as np
r,c=map(int,input().split())       # r is no. of rows and c is no. of columns
arr=np.eye(r,c)
print(arr)
