def tonum(count):
    return (count - 1) // 3


def check(n, k, logdivl):
    divl = 2**logdivl

    min_k = 2**(logdivl+1) - 2 - logdivl
    # print(divl * divl, divl * divl - (2*divl - 1), ((2**(n-logdivl))**2 - 1))
    max_k = tonum(divl * divl + (divl * divl - (2*divl - 1)) * ((2**(n-logdivl))**2 - 1))
    # print(n,k,logdivl, min_k, max_k)
    return min_k <= k <= max_k

def main(n, k):
    if k == 1:
        return n - 1

    if n > 100:
        return n - 1

    if ((2 ** (n-1)) ** 2 - 1) // 3 + 1 >= k:
        return n -1

    for logdivl in range(1, n+1):
        if check(n, k, logdivl):
            return n - logdivl

    return None


t = int(input())
for i in range(t):
    n, k  = list(map(int, input().split()))
    ans = main(n, k)
    if ans is not None:
        print("YES {}".format(ans))
    else:
        print("NO")
