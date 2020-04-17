import math
num=int(input("enter any number:"))
if num>1:
    for i in range(2,math.ceil(num/2)):
        if num%i==0:
            print("It is  not a prime number")
            break
        else:
            print("It is  a prime number")
else:
    print("It is not a prime")
