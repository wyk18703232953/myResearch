a = list(map(int,input().split()))
if a.count(1)>=1 or a.count(2)>=2 or a.count(3)==3 or (a.count(2)==1 and a.count(4)==2):
    print("YES")
else:
    print("NO")