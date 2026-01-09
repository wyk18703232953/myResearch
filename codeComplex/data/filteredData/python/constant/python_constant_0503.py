def main(n):
    # n: number of test cases (q)
    q = n
    results = []

    for i in range(q):
        # Deterministic generation of (n, m, k) for each test case
        ni = i - n // 2
        mi = (n - i) - n // 2
        ki = (i % (n + 2)) + 1 if n > 0 else 1

        n_val, m_val, k = ni, mi, ki

        if k == 0:
            if n_val == 0 and m_val == 0:
                results.append(0)

            else:
                results.append(-1)
        elif k == 1:
            if max(abs(n_val), abs(m_val)) != 1:
                results.append(-1)
            elif abs(n_val) == abs(m_val) == 1:
                results.append(1)

            else:
                results.append(0)

        else:
            if max(abs(n_val), abs(m_val)) > k:
                results.append(-1)
            elif abs(n_val) == abs(m_val):
                if (k - abs(n_val)) % 2 == 0:
                    results.append(k)

                else:
                    results.append(k - 2)
            elif (max(abs(n_val), abs(m_val)) - min(abs(n_val), abs(m_val))) % 2 == 0:
                if (k - max(abs(n_val), abs(m_val))) % 2 == 0:
                    results.append(k)

                else:
                    results.append(k - 2)

            else:
                results.append(k - 1)

    for ans in results:
        # print(ans)
        pass
if __name__ == "__main__":
    main(10)