import math
x=int(input("enter any number:"))
if x>1:
    for i in range(2,x):
        if x%i==0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
else:
    print("It is not a prime number")
        
