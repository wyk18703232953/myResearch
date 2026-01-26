n, k = map(int, input().split())
m = 1000000007
if n == 0:
    print(0)
    exit(0)
r = pow(2, k+1, m)*n - pow(2, k, m) + 1
print(r % m)
