class Parent:
     def __init__(self,fname):
          self.firstname=fname
     def printname(self):
          print(self.firstname)

class Student(Parent):
      def __init__(self,fname):
           Parent.__init__(self,fname) 

x=Student("Ram")
x.printname()