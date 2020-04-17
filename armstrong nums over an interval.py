lower=int(input("enter any number:"))
upper=int(input("enter any number:"))


for num in range(lower,upper+1):
    flag=0
    temp=num
    n=len(str(num))
    for i in range(n):
        
        digit=temp%10
        z=digit**n
        flag=flag+z
        temp//=10
    if num==flag:
        print(num,"armstrong number")
    else:
        print(num,"not an armstrong number")
        
    
