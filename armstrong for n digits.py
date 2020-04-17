num=int(input("enter any number"))
x=len(str(num))
flag=0
temp=num
i=0
while i<x:
    digit=temp%10
    y=digit**x
    flag=flag+y
    temp=temp//10
    i=i+1
    
if num==flag:
    print("armstrong number")
else:
    print("not an armstrong number")
