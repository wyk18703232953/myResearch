t = int(input())

def sol(n, k):
    p = 1
    acc = 0
    while n > 0 and k >= p:
        k -= p
        n -= 1
        if n >= 40:
            return n
        acc += (2*p-1)*(4**n-1)//3
        if k <= acc:
            return n
        p = 2*p+1
    return -1

for _ in range(t):
    n, k = (int(v) for v in input().split())
    ans = sol(n, k)
    if ans == -1:
        print("NO")
    else:
        print("YES", ans)