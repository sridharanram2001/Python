
def add(a,b):
   c=a+b
   print(f"Adding {a} and {b}")
   return c

def subtract(e,f):
    g=e-f
    print(f"Subtracting {e} and {f} ")
    return g

def multiply(h,i):
    j=h*i
    print(f"Multiplying {h} and {i} ")
    return j

def divide(k,l):
    m=k/l
    print(f"Dividing {k} and {l}")
    return m    

def none():
     print("Enter a number between 1 to 4")
     main() 

def main():
  print("1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
  number=input("Enter a number to perform the operation")
  no1=input("Enter the first number");
  no2=input("Enter the second number");

  if(number==1):
    {
      answer=add(no1,no2)
      print(f"Result = {answer}")
    }
  elif(number==2):
   {
     answer=subtract(no1,no2)
     print(f"Result = {answer}")
    }
  elif(number==3):
   {
     answer=multiply(no1,no2)
     print(f"Result = {answer}")
   }
  elif(number==4):
   { 
     answer=divide(no1,no2)
     print(f"Result = {answer}")
   }
  elif(number==5):
   {
     return 0
   }
  else:
   {
     none()
   } 
 
main()
  