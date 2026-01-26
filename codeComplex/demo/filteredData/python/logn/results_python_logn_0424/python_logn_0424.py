def main(n):
    # Interpret n as number of test cases
    case = n

    for t in range(case):
        # Deterministically generate (n_local, k) for each test case
        # Ensure n_local is at least 1 and at most 31 (since arrays are size 32)
        n_local = (t % 30) + 1  # 1..30
        # Generate k based on t and n_local; keep it within a reasonable range
        # Use powers of 2 pattern to exercise branches
        k = (1 << ((t % 20) + 1)) - 1

        f = [0] * 32
        g = [0] * 32
        success = False
        ans = n_local

        for i in range(1, n_local):
            f[i] = f[i - 1] * 4 + 1
            if f[i] >= k:
                success = True
                break

        for i in range(1, n_local + 1):
            if k < (1 << i) - 1:
                break
            k = k - (1 << i) + 1
            ans = ans - 1

        for i in range(n_local - 1, ans - 1, -1):
            if i >= 32 or (i and f[i] == 0):
                success = True
                break
            g[i] = 1 if i == n_local - 1 else g[i + 1] * 2 + 3
            k = k - f[i] * g[i]
            if k <= 0:
                success = True
                break

        if success:
            # print("YES %d" % ans)
            pass

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    main(10)