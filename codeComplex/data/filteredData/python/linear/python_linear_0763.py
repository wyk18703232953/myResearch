from collections import deque

def main(n):
    # Interpret n as both array length and number of queries for scalability
    # Generate deterministic nums: a simple permutation where max is at the end
    # nums = [2, 3, 4, ..., n, 1]
    if n < 2:
        # Degenerate small case: ensure at least 2 elements
        nums = [1, 1]
        m = 1

    else:
        nums = list(range(2, n + 1)) + [1]
        m = n

    mxnum = max(nums)
    d = deque(nums)

    # Deterministic queries: q = 1..m
    qr = list(range(1, m + 1))

    log = []
    rot = 0

    while True:
        a = d.popleft()
        b = d.popleft()
        log.append((a, b))
        if a > b:
            a, b = b, a
        d.append(a)
        d.appendleft(b)
        rot += 1
        if b == mxnum:
            break

    for q in qr:
        if q <= rot:
            # print(log[q - 1][0], log[q - 1][1])
            pass

        else:
            res = q - rot - 1
            # print(b, d[res % (n - 1) + 1])
            pass
if __name__ == "__main__":
    main(10)