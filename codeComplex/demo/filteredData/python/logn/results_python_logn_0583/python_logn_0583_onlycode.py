def formula(n, x):
    return x*(x + 1)//2 - (n-x)

def solve():
    n, k = map(int, input().split())
    l = 1
    r = n
    x = 0
    while l <= r:
        x = (l+r)//2
        res = formula(n, x)
        if res == k:
            break
        elif res < k:
            l = x + 1
        else:
            r = x - 1
    print(n-x)
    return

solve()