n=int(input())
a=[]
for i in range(n+1):
    a.append(((n+1)-i)*i)
print(max(a))