def fib(x):
    a=0
    b=1
    

    if x<1:
        print("enter any positive number")
    elif x==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(3,x+1):
            a,b=b,a+b
            print(b)
fib(5)
