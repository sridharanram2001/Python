print(''' You Enter a Dark Room with two doors.Which
two doors would you select 1 or 2''')

door=input(">>")
if(door=="1"):
      print("There is a giant bear eating a cheese cake")
      print("What do you do?")
      print("1.Take the cake")
      print("2.Scream at the bear")
      bear=input(">>")
      
      if(bear=="1"):
                 print("The bear eats your face off.Good job!")
      elif(bear=="2"):
                 print("The bear eats your legs off.Good job!")
      else:
                 print(f"Well done {bear} is a good option")
                 print("Bear runs away")
elif(door=="2"):
      print("You stare into the endless abyss at Cthulhu's retina")
      print("1.Blueberries")
      print("2.Yellow jacket clothspins")
      print("3.Understanding revolver yelling melodies")

      insanity=input(">>")
      if(insanity==1):
            print("Your body survives powered by a mind of jello")
      elif(insanity==2):
            print("Good job!")
      else:
            print("The insanity rots your eyes into a pool of muck ")
            print("Good job")
else:
          print("You stumble around fall on a knife and die")