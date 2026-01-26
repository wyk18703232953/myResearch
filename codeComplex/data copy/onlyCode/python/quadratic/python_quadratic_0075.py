n = int(input())
l = list(map(int, input().split()))
odd = 0
for i in range(n):
    for j in range(i, n):
        if(l[i]>l[j]): odd ^= 1
 
m = int(input())
ans = []
for i in range(m):
    ll, r = map(int, input().split())
    k = r-ll+1
    if( (k*(k-1)/2) %2): odd ^= 1
    ans.append( "odd" if odd else "even")
 
print('\n'.join(ans))