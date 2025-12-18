n=int(input())
l=sorted(list(map(int,raw_input().split())))
def f():
    global n
    dou=False
    for k in range(1,n):
        if l[k]==l[k-1]:
            if dou or l[k]==0 or (l[k]==l[k-2] and n!=2) or l[k]==l[k-2]+1:
                return False
            else:
                dou=True
    return (sum(l)-(n*(n-1))//2)%2
if f():
    print("sjfnb")
else:
    print("cslnb")
