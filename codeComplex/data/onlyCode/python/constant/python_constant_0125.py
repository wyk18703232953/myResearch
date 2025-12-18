n=int(input())
m=str(n)
print(max(int(m),int(m[:-2]+m[-1:]),int(m[:-1])))
