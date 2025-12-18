n,p,l,r = map(int,input().split())
if l == 1 and r == n:
    print(0)
elif l==1:
    print(abs(p-r)+1)
elif r == n:
    print(abs(p - l) + 1)
else:
    print(min(abs(p-r),abs(p - l))+r-l+2)