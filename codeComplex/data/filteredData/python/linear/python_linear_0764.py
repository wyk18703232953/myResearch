import sys

def main(n):
    # Ensure n is at least 2 to have meaningful n,q and array a
    if n < 2:
        n = 2

    # Deterministic generation of n, q, and array a based on input scale n
    # Here:
    #   logical_n = n  (used as original problem's n)
    #   q = n          (number of queries scales with n)
    logical_n = n
    q = n

    # Generate array a of length logical_n
    # Make it non-trivial: first half increasing, second half decreasing
    a = []
    half = logical_n // 2
    for i in range(half):
        a.append(i + 1)
    for i in range(logical_n - half):
        a.append(half + (logical_n - half) - i)

    # Core logic from original program (no input())
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

    # Generate q deterministic query times tm based on n and q
    # Use a simple pattern that covers various ranges:
    #   tm values from 1 up to (2*q), wrapped to be at least 1
    queries = []
    for i in range(1, q + 1):
        tm = (i * 2)
        if tm < 1:
            tm = 1
        queries.append(tm)

    # Process queries and print results
    for tm in queries:
        if 1 <= tm <= t:
            # print(Lis[tm - 1][0], Lis[tm - 1][1])
            pass

        else:
            # print(max_a, anslist[(tm - t - 1) % len(anslist)])
            pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)