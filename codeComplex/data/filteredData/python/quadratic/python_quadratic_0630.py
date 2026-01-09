def main(n):
    mod = 1000000007

    # Deterministically generate input for problem A
    # Interpret n as the length of the array
    if n <= 0:
        return
    a = [(i + 1) * (1 + (i % 5)) for i in range(n)]

    # Core logic from A()
    a.sort()
    f = [1] * n
    p = 0
    ans = 0
    while p < n:
        while p < n and not f[p]:
            p += 1
        if p == n:
            break
        ans += 1
        for i in range(n):
            if a[i] % a[p] == 0:
                f[i] = 0
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)