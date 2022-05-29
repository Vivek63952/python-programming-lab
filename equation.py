# program to find the roots of quadratic equations
import cmath
  
a = 1
b = 4
c = 2
  

dis = (b**2) - (4 * a*c)
  

root1 = (-b-cmath.sqrt(dis))/(2 * a)
root2 = (-b + cmath.sqrt(dis))/(2 * a)
  

print('The roots are')
print(root1)
print(root2)
