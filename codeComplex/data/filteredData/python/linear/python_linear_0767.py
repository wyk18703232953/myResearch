def main(n):
    from collections import deque

    # Define problem size mapping:
    # n: size of array
    # q: number of queries
    if n <= 1:
        n = 2
    q = n

    # Deterministic array generation: permutation-like pattern
    # Make sure max element is at the end to exercise the loop
    arr = [((i * 3) % n) + 1 for i in range(n - 1)]
    arr.append(n)
    maxval = max(arr)

    d = deque(arr)
    ans = {}
    count = 1

    # Simulate until maxval reaches the front
    while d[0] != maxval:
        a = d.popleft()
        b = d.popleft()
        ans[count] = (a, b)
        count += 1
        if a > b:
            d.append(b)
            d.appendleft(a)

        else:
            d.append(a)
            d.appendleft(b)

    # Now d[0] == maxval, the rest forms a cycle
    cycle = list(d)[1:]  # elements after maxval
    cycle_len = len(cycle)

    # Deterministic generation of query list
    # Queries cover:
    # - first few steps (<= count)
    # - some beyond count to hit the cyclic behavior
    queries = []
    # first half: within [1, count]
    for i in range(1, min(q // 2 + 1, count + 1)):
        queries.append(i)
    # second half: beyond count, including multiple wraps
    base = max(count, 1)
    while len(queries) < q:
        queries.append(base + len(queries) - (len(queries) // 2))

    # Process queries as original logic
    for m in queries:
        if m in ans:
            # print(ans[m][0], ans[m][1])
            pass

        else:
            k = m - count
            idx = (k % cycle_len)
            # print(maxval, cycle[idx])
            pass
if __name__ == "__main__":
    main(10)