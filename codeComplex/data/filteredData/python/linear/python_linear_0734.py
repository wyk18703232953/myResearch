def main(n):
    from collections import deque

    # Scale mapping:
    # N = n (queue size), Q = n (number of queries)
    # Queue contents: 1..N
    # Queries: 1..Q
    N = max(2, n)  # ensure N >= 2 to avoid division by zero in (N-1)
    Q = n

    que = deque(range(1, N + 1))
    ma = max(que)

    X = []
    k = -1
    c = 0
    # The original condition: while c <= k+N+5
    # We run the same structure, but must ensure it terminates deterministically.
    # Here, we rely on the fact that with this process k will be set once max reaches front.
    # To be safe for very small N, we add an upper bound proportional to N.
    upper_bound = 5 * N + 10
    while c <= k + N + 5 and c <= upper_bound:
        a = deque.popleft(que)
        b = deque.popleft(que)

        X.append((a, b))
        c += 1
        if a > b:
            a, b = b, a
        if k < 0 and b == ma:
            k = c
        deque.appendleft(que, b)
        deque.append(que, a)

    # In case k was never set (pathological for very small N), fall back to last c
    if k < 0:
        k = c - 1 if c > 0 else 0

    # Generate Q queries deterministically: 1..Q
    queries = list(range(1, Q + 1))

    results = []
    for qi in queries:
        i = qi - 1
        if i <= k:
            results.append(f"{X[i][0]} {X[i][1]}")

        else:
            if N - 1 > 0:
                idx = (i - k) % (N - 1) + k

            else:
                idx = k
            results.append(f"{X[idx][0]} {X[idx][1]}")

    # For timing experiments, usually you just want the work done; printing is optional.
    # Here we return the results so the caller can decide what to do.
    return results


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    out = main(10)
    for line in out:
        # print(line)
        pass