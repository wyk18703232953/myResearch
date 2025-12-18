a,b=input().split()
if(a==b):
    print("0")
else:
    xor=bin(int(a)^int(b))[2:]
    a=bin(int(a))[2:]
    b=bin(int(b))[2:]
    ans=""
    if a[0]==b[0]:
        ans+="0"
    else:
        ans+="1"
    for i in range(len(xor)):
        ans+="1"
    print(int(ans,2))
