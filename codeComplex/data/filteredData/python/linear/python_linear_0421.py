def main(n):
    # Deterministically construct x and arr based on n
    x = (n // 2) ^ (n * 3)
    if x == 0:
        x = 1

    # Generate an array of length n with deterministic pattern
    # Ensure values are within bounds of arrays sized 100100
    MOD = 100000
    arr = [((i * 17 + n * 31) ^ (i * i + 7)) % MOD for i in range(n)]

    f = [0] * 100100
    s = [0] * 100100
    can = [False] * 100100

    for i in range(n):
        val = arr[i]
        ax = val & x
        f[val] += 1
        s[ax] += 1
        if ax != val:
            can[ax] = True

    ans = 3
    limit = 100100
    for i in range(limit):
        if f[i] >= 2:
            ans = 0
            break
        if f[i] == 1 and s[i] >= 1:
            if can[i]:
                if ans > 1:
                    ans = 1
        if s[i] >= 2:
            if ans > 2:
                ans = 2

    if ans == 3:
        # print(-1)
        pass

    else:
        # print(ans)
        pass
if __name__ == "__main__":
    main(10000)