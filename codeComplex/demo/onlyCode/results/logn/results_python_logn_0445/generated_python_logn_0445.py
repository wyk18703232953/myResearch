def sol(n, k):
    p = 1
    q = 1
    acc = 0
    while n > 0 and k >= p:
        k -= p
        n -= 1
        if n >= 40:
            return n
        acc += q * (4 ** n - 1) // 3
        if k <= acc:
            return n
        p = 2 * p + 1
        q = 2 * q + 3
    return -1

def main(n):
    results = []
    for i in range(n):
        ni = max(1, i + 1)
        ki = (i + 2) * 3
        ans = sol(ni, ki)
        if ans == -1:
            results.append(("NO",))
        else:
            results.append(("YES", ans))
    return results

if __name__ == "__main__":
    out = main(5)
    for r in out:
        print(*r)