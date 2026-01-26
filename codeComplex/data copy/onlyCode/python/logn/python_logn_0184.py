def func(mid,s):
    p=0
    q=mid
    while (mid>0):
        p+=mid%10
        mid=mid//10

    if (q-p)>=s:
        return True
    else:
        return False
n,s=map(int,input().split())
do=1
up=10**18
an=n+1
while (up>=do):
    mid=(up+do)//2
    if func(mid,s):
        up=mid-1
        an=mid
    else:
        do=mid+1
if an>n:
    print(0)
else:
    print(n-an+1)