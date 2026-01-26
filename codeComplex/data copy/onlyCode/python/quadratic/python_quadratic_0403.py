n,k = map(int,input().split())
t = input()
if n==1:
    print(t*k)
else:
    i = len(t)-1
    while i>0 and t[-i:] != t[:i]:
            i-=1
    t2 = t[i:]
    print(t+t2*(k-1))