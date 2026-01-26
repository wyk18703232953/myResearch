m=int(1e9+7)

def solve(x, k):
    return (m+(pow(2, k, m)*x%m)%m-((pow(2, k, m)-1)%m*pow(2, m-2, m)%m)%m)%m;
    
x,k=[int(x) for x in input().split()]

if x==0:
    print(0)
elif k==0:
    print((m+2*(x%m))%m)
else:
    print((m+2*solve(x, k))%m)
