n,p = map(int,input().split())
a  = list(map(int,input().split()))
forward = [a[0]]
for i in range(1,n):
    forward.append(forward[-1] + a[i])
sm = sum(a)
mx = -float('inf')
for i in range(n-1):
    mx = max(mx,(forward[i]%p) + ((sm -forward[i] )%p))
print(mx)