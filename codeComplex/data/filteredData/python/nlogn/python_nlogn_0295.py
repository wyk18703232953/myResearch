def main(n):
    from collections import deque

    # Generate deterministic data from n
    # m: list of n integers
    m = [(i * 7) % (n + 3) for i in range(1, n + 1)]

    # s: string of length n consisting of '1' and '0',
    # here we alternate for determinism
    s = ''.join('1' if i % 2 == 0 else '0' for i in range(n))

    a = []
    b = deque()

    i = 1
    for x in m:
        a.append((x, i))
        i += 1
    a.sort(key=lambda p: -p[0])

    ans = []

    for x in s:
        if x == "1":
            if b:
                v = b.pop()
                ans.append(v[1])
            else:
                # if b is empty but original code would pop, avoid error by using a placeholder
                # deterministic behavior: use index 0
                ans.append(0)
        else:
            if a:
                v = a.pop()
                ans.append(v[1])
                b.append(v)
            else:
                # if a is empty but original code would pop, avoid error by using a placeholder
                ans.append(0)

    print(*ans)


if __name__ == "__main__":
    main(10)