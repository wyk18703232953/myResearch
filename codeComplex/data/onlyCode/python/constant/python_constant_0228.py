a,b = map(int, input().split())
x, y, z = map(int, input().split())

ans = max(0, 2*x+y-a)+max(0, 3*z+y-b)
print(ans)
