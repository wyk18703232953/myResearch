def substraction(a,b):
    if a==0 or b==0:
        return 0
    else:
        if a>b:
            count=a//b
            return substraction(a%b,b)+count
        else:
            count = b//a
            return substraction(a,b%a)+count

t=int(input())
lst=[]
res=[]
for i in range(0,t):
    lst=[int(i) for i in input().split()]
    ele=substraction(lst[0],lst[1])
    res.append(ele)

for i in range(0,t):
    print(res[i])