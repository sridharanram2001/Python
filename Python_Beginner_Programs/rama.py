hours =int(input('enter the hours'))
rate= float(input('enter the rate'))
if(hours<=40):
    print(hours*rate)
else:
    print((1.5*rate*(hours-40))+(40*rate))
