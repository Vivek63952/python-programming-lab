#Proram to find no. of characters, words and lines in "data.txt" file

f=open("data.txt",mode='r')
no_of_words=0
no_of_chars=0
no_of_lines=0
for line in f:
    no_of_lines+=1
    line=line.strip("\n")
    no_of_chars+=len(line)
    list1=line.split()
    no_of_words+=len(list1)
f.close()
print("number of line:",no_of_lines)
print("number of words:",no_of_words)
print("number of characters:",no_of_chars)
