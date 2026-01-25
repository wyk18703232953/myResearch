def main(n):
    # Ensure n is at least 1
    if n <= 0:
        print("NO")
        return

    # Deterministically generate a sequence of n digits as characters
    # Pattern: a[i] = (i % 10)
    a = [str(i % 10) for i in range(n)]

    smm = 0
    for i in range(n):
        a[i] = int(a[i])
        smm += a[i]

    ans = "NO"
    sm = smm
    for div in range(2, n + 1):
        sm = smm
        if not sm % div:
            sm //= div
            f = 0
            s = 0
            for i in range(n):
                s += a[i]
                if s == sm:
                    s = 0
                    f += 1
            if f == div:
                ans = "YES"
                break
    print(ans)


if __name__ == "__main__":
    # Example deterministic call; change n for different scales
    main(10)