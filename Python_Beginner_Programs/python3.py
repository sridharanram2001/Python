
fop=open("file3.txt","w+")
line1="This is a file"
fop.write(line1)
print(fop.read())
print("Now I will truncate the file")
fop.truncate()
line2="This is the new sentence"
fop.write(line2)
print(fop.read()) 
fop.flush()