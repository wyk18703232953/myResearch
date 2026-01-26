n,k = [int(x) for x in input().split()]
a = []
for _ in range(n):
    a.append([int(x) for x in input().split()])

a.sort(key = lambda x: x[1])
a.sort(reverse=True,key=lambda x: x[0])
b=a[k-1] 
print(a.count(b))