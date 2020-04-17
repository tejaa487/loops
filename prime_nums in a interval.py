x=int(input("enter the 1st number"))
y=int(input("enter the 2nd number"))
for num in range(x,y+1):
    if x>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

else:
    print("lower limit(x) should be>2")
