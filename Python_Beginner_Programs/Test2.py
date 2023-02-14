import sys
from os.path import exists
a=sys.argv
print("Lets see if the file exists ")
print(f"The file is {exists(a)}") 
try11=open("a",r)
print(try1)
print("Now we are truncatiing the file ")
try1.truncate()
try1.close()
try2=open("a",w)
dat1=input("Enter a data")
try2.write(dat1)
try2.close()
#try3=open("fileA.txt",w+)
#try3.seek(2) 