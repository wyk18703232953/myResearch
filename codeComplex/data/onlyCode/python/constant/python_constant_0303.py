k,n,s,p = map(int, input().split())
q = (n+s-1)//s
ans = (q*k+p-1)//p
print(ans)
