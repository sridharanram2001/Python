file1=open("practicefile1.txt","r+")
print(file1.read())
file1.seek(0)
file1.truncate()
file1.seek(0)
file1.write("Hello")
file1.seek(0)
print(file1.read())
file1.close()


