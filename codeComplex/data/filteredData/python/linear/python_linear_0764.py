def main(n):
    # n controls both array size and number of queries
    # Ensure minimum sizes to avoid edge cases
    n = max(2, n)

    # Deterministic generation of n, q, and array a
    # Let array length be n, number of queries be n
    N = n
    q = n

    # Generate array a of length N with some variability
    # Example: a[i] = (3*i + 7) % (2*N) + 1 ensures positive numbers and a max exists
    a = [((3 * i + 7) % (2 * N)) + 1 for i in range(N)]

    # Original logic starts here (with n,q,a defined deterministically)

    max_a = max(a)
    t = a.index(max_a)
    last = a[0]
    Lis = []
    tmp = []
    for i in range(1, t + 1):
        Lis.append((last, a[i]))
        if last < a[i]:
            tmp.append(last)
            last = a[i]

        else:
            tmp.append(a[i])

    anslist = a[t + 1:] + tmp

    # Deterministic generation of queries:
    # Use values that cover ranges below, within, and above t
    # For i in range(q), define tm deterministically from i and t
    res = []
    if len(anslist) == 0:
        # Edge case: if anslist is empty, avoid modulo by zero
        # This only happens if t == N-1 and tmp is empty
        for i in range(q):
            tm = i + 1
            if 1 <= tm <= t:
                res.append(f"{Lis[tm - 1][0]} {Lis[tm - 1][1]}")

            else:
                res.append(f"{max_a} {max_a}")

    else:
        L = len(anslist)
        for i in range(q):
            # Construct tm such that it spans different regions
            # Example pattern: cycles through [1, t, t+1, ..., t+L]
            tm = (i % (t + L + 1)) + 1
            if 1 <= tm <= t:
                res.append(f"{Lis[tm - 1][0]} {Lis[tm - 1][1]}")

            else:
                res.append(f"{max_a} {anslist[(tm - t - 1) % L]}")

    # Output the results
    for line in res:
        # print(line)
        pass
if __name__ == "__main__":
    main(10)