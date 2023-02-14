a = int(input("Enter the input 1 : "))
b = int(input("Enter the input 2 : "))
c = int(input("Enter the input 3 : "))
d = int(input("Enter the input 4 : "))
e = int(input("Enter the input 5 : "))
f = int(input("Enter the input 6 : "))

output1 =a and b
output2 =c and d

output3 =output1 and output2

output4 =e or f
output4 =not output3

output5=output4 and output3

output6 =not output5

if(output6 == True):
	output6=1
else:
	output6=0

print(output6) 