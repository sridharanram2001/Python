mean = 0
median = 0
mode = 0
n = int(input())
x = input().split(" ")
arr = list()
for i in range(0,len(x)):
    num = int(x[i])
    arr.append(num)
for i in range(0,len(arr)):
    mean = (arr[i]/len(arr)) + mean

for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            

if(len(arr)%2 == 0):
    c = int(len(arr)/2)
    d = c-1
   
    median = (arr[c]+arr[d])/2    
else:
    a = round(len(arr)/2)
    ++a
    median = arr[a]

dict1 = dict()

for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if(arr[i]==arr[j]):
            dict1[arr[i]]+=1  

print(mean)
print(median)
print(mode)