def main(n):
    # Interpret n as: number of elements and number of queries both equal to n
    # Deterministically generate nums and queries
    # nums: length n, some varying pattern
    nums = [(i * 2 + 3) % (3 * n + 7) + 1 for i in range(n)]
    # Ensure there is some variation and a clear maximum
    if n > 0:
        nums[0] = n * 5 + 10
    # queries: first n positive integers
    queries = list(range(1, n + 1))

    q = len(queries)

    if n == 0:
        return

    m = max(nums)
    ab = []
    # simulate until max element reaches front
    from collections import deque
    dq = deque(nums)
    while dq[0] < m:
        ab.append([dq[0], dq[1]])
        if dq[0] > dq[1]:
            first = dq.popleft()
            dq.popleft()
            dq.append(first)

        else:
            first = dq.popleft()
            dq.append(first)
    nums_after = list(dq)

    for i in range(q):
        mj = queries[i]
        if mj <= len(ab):
            a, b = map(str, ab[mj - 1])

        else:
            a, b = map(
                str,
                (
                    m,
                    nums_after[(mj - len(ab) - 1) % (len(nums_after) - 1) + 1],
                ),
            )
        # print(a + " " + b)
        pass
if __name__ == "__main__":
    main(10)