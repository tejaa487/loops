x=int(input("enter the number of terms"))
n1=0
n2=1
if x<0:
    print("enter any positive integer")
elif x==1:
    print(n1)
else:
    print(n1)
    print(n2)
    for i in range (1,x-1):
        
        n1,n2=n2,n1+n2
        print(n2)
        
