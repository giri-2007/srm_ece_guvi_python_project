a = input("enter a value")
if a.isdigit() :
    print(f" {a} is digit")
elif a.isalpha() :
    print(f" {a} is alphabet")
else :
    print(f" {a} is special character")