from sys import argv
from os.path import exists
script,from_file,to_file=argv

print(f"Copying contents of the file {from_file} to {to_file}")

file1=open(from_file)
data1=file1.read()
print(f"The input file is {len(data1)} bytes long ")
print(f"Does the file exist? {exists(to_file)}")

file2=open(to_file,'w')
file2.truncate()
file2.write(data1)

print("All right all done ")

file1.close()
file2.close() 
