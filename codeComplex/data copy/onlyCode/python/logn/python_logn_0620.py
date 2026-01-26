# n = nPUT + nEAT
# k = nPUT(nPUT+1)/2 - nEAT
# nPUT = n - nEAT
# k = (n - nEAT)(n - nEAT + 1)/2 - nEAT
# k = (n - x)(n - x + 1)/2 - x

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

n, k = list(map(int, input().split(' ')))
answer = int((-1/2) * isqrt(8*k + 8*n + 9) + n + 3/2)

print(answer)
