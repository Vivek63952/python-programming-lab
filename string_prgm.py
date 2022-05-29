
# Python program to capitalize first and last character of  each word of a String
  
  
def word_both_cap(str):
      
  
    return ' '.join(map(lambda s: s[:-1]+s[-1].upper(), 
                        s.title().split()))
         

s =input("pls enter a string")
print("String before:", s)
print("String after:", word_both_cap(str))
