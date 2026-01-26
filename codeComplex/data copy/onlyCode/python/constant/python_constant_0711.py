n, v = list(map(int, input().split()))
f = lambda x: x*(x+1)//2
print(min(n-1, v)+f(n-min(n-1, v))-1)