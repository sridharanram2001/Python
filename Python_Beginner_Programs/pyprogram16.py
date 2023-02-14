from sys import argv
script,filename=argv

print(f"We are going to erase {filename}")

my_file=open(filename,'w')

print("Now I am opening the file ..")

print("And now I am truncating ")

my_file.truncate()
my_file.close()

print("Now I am going to add the given lines")
my_file=open(filename,"w")
line1=input("Line 1:")
line2=input("Line 2:")
line3=input("Line 3:")

my_file.write(line1)
my_file.write("\n")
my_file.write(line2)
my_file.write("\n")
my_file.write(line3)
my_file.write("\n")

print(my_file.read)
print("And now we finally close")
my_file.close()