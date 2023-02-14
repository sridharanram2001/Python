  
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"You have {cheese_count} cheeses");
    print(f"You have {boxes_of_crackers} box of crackers");
    print("Man thats enough for a party ");
    
 
   print("Giving arguments"):
   cheese=int(input("Enter the number of cheese slices"));
   crackers=int(input("Enter thev number of cracker boxes"));
  
    cheese_and_crackers(cheese,crackers)
  
    print("We can also do math while giving arguments")
    cheese_and_crackers(10+6,20+3)

    print("We can also add variables to these numbers")
    cheese_and_crackers(cheese+10,crackers+12); 