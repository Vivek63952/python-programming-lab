#PROGRAM GENERATE 4 INTEGERS B/W 10 AND 99 WHICH IS DIVISIBLE BY 5
import random

print("Generating 4 random integer number between 10 and 99 divisible by 5")
for num in range(4):
    print(random.randrange(10, 99, 5), end=', ')
