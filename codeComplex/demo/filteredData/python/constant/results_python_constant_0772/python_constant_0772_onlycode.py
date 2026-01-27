t=int(input())
for i in range(t):
    n=int(input())
    g=list(map(int,input().split()))
    m1=max(g)
    g.remove(m1)
    m2=max(g)
    dl=len(g)-1
    print(min(dl,m2-1))