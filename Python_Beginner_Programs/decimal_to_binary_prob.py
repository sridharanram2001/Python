def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2,end=' ')



input1 = int(input("Enter the first input : "))
input2 = int(input("Enter the second input : "))

input1 = decimalToBinary(input1)
input2 = decimalToBinary(input2)

print(input1)
print("\n",input2)