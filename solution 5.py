a = int(input("enter a value"))

if a >1:
     prime = True
     for i in range(2,a):
       if a %i == 0 :
        prime = False
        break
     if prime:
          print(" prime")
     else :
          print(" not a prime")
else :
    print("not a prime")
