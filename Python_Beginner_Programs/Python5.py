def boxvolume(l,b,h):
       volume=l*b*h
       return volume
a=int(input("Enter the length of the box"))
b=int(input("Enter the breadth of the box"))
c=int(input("Enter the height of the box"))
d=boxvolume(a,b,c)
print(d)