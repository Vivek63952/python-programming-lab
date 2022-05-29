#Program to copy content of file into another file "first.txt,second.txt"
f1=open("first.txt",mode='r')
f2=open("second.txt",mode='w')
data=f1.readlines()
for line in data:
      f2.write(line)
f1.close()
f2.close()
