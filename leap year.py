x=int(input("enter any number:"))
if x%4==0:
    if x%100==0:
        if x%400==0:
            print(x,"is leap year")
        else:
            print(x,"is not a leap year")
    else:
        print(x,"is leap year")
else:
    print(x,"is not leap year")
