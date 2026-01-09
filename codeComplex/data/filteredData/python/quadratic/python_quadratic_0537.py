def main(n):
    N = 55
    f = [0]
    for i in range(1, N):
        f.append(f[-1] * 4 + 1)
        if f[-1] > 1e18:
            break

    # Interpret n as number of test cases
    t = n

    # Deterministic generation of (n_i, m_i) for each test case
    results = []
    for ca in range(t):
        # Generate n_i in [1, 40] to cover both branches (<=31 and >31)
        n_i = (ca % 40) + 1
        # Generate m_i in a deterministic but varying way
        # Keep it within a reasonable range depending on n_i
        m_i = (ca * ca + n_i * 17) % (10**6 + n_i)

        n_val = n_i
        m_val = m_i

        if n_val > 31:
            results.append("YES {}".format(n_val - 1))

        else:
            start = 0
            found = False
            res = -1
            for i in range(1, n_val + 1):
                start += 2**i - 1
                end = start
                for k in range(1, i + 1):
                    end += f[n_val - k] * (2 ** (k + 1) - 3)
                if m_val >= start and m_val <= end:
                    found = True
                    res = i
                    break
            if found:
                results.append("YES {}".format(n_val - res))

            else:
                results.append("NO")

    # To keep side effects similar to original, print results
    for line in results:
        # print(line)
        pass
if __name__ == "__main__":
    main(10)