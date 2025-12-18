n,p,v = input().split()
x= list(map(int,input().split()))

x.sort()
print(x[int(v)]-x[int(v)-1])