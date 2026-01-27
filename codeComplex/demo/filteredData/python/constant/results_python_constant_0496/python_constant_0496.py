def main(n):
    q = n
    results = []
    for i in range(q):
        x = i
        y = 2 * i + 1
        k = 3 * i + 2
        if x > y:
            x, y = y, x
        m = y
        d = y
        if (y - x) % 2 == 1:
            d -= 1
        if k < m:
            results.append(-1)
            continue
        r = k - m
        if r % 2 != 0:
            r -= 1
            if d != m:
                d += 1

            else:
                d -= 1
        d += r
        results.append(d)
    for v in results:
        # print(v)
        pass
if __name__ == "__main__":
    main(10)