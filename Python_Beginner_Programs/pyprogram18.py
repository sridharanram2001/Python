def print_two(*args): # Takes two arguments 
    arg1,arg2=args
    print(f"Argument1={arg1} , Argument={arg2}");

def print_two_again(*args):
   arg3,arg4=args
   print(f"Argument3={arg3} , Argument4={arg4}")

def print_one(str1):
   print(str1)

def print_none():
   
     print("--------------- ")
   
print_two("Ram","Prakash")
print_two_again("Rama","Preethi")
print_one("Twins")
print_none()
 