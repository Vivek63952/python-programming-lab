# PROGRAM TO CHECK LIST IS EMPTY OR NOT
def empty_or_not(lis1):
    if not lis1:
        return 1
    else:
        return 0
          

lis1 = []
if empty_or_not(lis1):
    print ("The list is Empty")
else:
    print ("The list is not empty")
