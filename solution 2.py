unit = int(input("enter units" ))
if unit <=100 :
    bill = 5*unit
    print(f"{bill} is your billamount")
elif unit <=200 :
    bill = 7*unit 
    print(f"{bill} is your billamount")
elif unit > 200 :
    bill = 10*unit
    print(f"{bill} is your billamount")
else :
    print("invalid input")