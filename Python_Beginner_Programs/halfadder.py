
input1=int(input("Enter input 1 : "))
input2=int(input("Enter input 2 : "))


if(input1==0 and input2==0):
	sum=0
	carry=0
elif((input1==0 and input2==1) or (input1==1 and input2==0)):
	sum=1
	carry=0
else:
	sum=1
	carry=1

print(f"Sum : {sum}")
print(f"\nCarry : {carry}")
		
