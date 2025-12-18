k = int(input())
n = 0
i = 0
while (k > n):
    n += pow(10, i) * 9 * (i + 1)
    i = i + 1
n -= pow(10, i - 1) * 9 * i
k -= n
t = (k - 1) / i
r = k % i
if (r == 0):
    r = i
m = pow(10, i - 1) + t
m = int(m)
ans = int(m / pow(10,i - r)) % 10
print(ans)

def pow(i):
    n = 1
    for x in range(0,i):
        n*=10
    return n

