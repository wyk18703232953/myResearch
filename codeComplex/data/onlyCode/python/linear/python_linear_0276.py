n,m,a,b=[int(x)for x in input().split()]
if n<m:print(min(a*(m-n),b*n))
else:print(min(b*(n%m),a*(m-(n%m)) ))