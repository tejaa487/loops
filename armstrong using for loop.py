
num=int(input("enter any num"))
y=len(str(num))
flag=0
temp=num
for i in range(y):
    digit=temp%10
    x=digit**y
    flag+=x
    temp//=10

if num==flag:
    print("armstrong number")
else:
    print("not an armstrong number")
    
    
