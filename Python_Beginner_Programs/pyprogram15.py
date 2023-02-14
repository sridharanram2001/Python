from sys import argv
script,filename=argv

print(script)
txt=open(filename)
print(f"Here is your filename {filename}")
print(txt.read())

print("Type the file name again")
file_again=input(">")

txt_again=open(file_again)
print(txt_again.read())
