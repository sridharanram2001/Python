print("Enter the length , breadth and height of the box ")
def boxvolume(a,b,c):
     
          volume=a*b*c;
          return(volume);
     
length=int(input("Enter the length :"))
breadth=int(input("Enter the breadth :"))
height=int(input("Enter the height :"))
output = boxvolume(length,breadth,height)
print(f"Your answer is {output} ")
 