def main(n):
    from heapq import heappush, heappop

    # Deterministic data generation
    # Map n to:
    #   - number of intervals = n
    #   - x and y as simple deterministic functions of n
    x = n + 5
    y = (2 * n + 3) or 1  # avoid zero

    a = []
    for i in range(n):
        # Generate a deterministic interval [u, v] with u < v
        u = i * 2
        v = u + (i % 5) + 1
        a.append((u, 1))
        a.append((v, -1))

    a.sort(key=lambda x: x[0] * 10000000000 - x[1])
    mod = 10 ** 9 + 7
    t, z, ans = 1, 1, x
    b = []
    for i in range(1, len(a)):
        z += a[i][1]
        if z < t:
            ans = (ans + t * (a[i][0] - a[i - 1][0]) * y) % mod
            heappush(b, -a[i][0])

        else:
            if b:
                if x < (a[i][0] + b[0]) * y:
                    ans = (ans + t * (a[i][0] - a[i - 1][0]) * y + x) % mod

                else:
                    ans = (ans + t * (a[i][0] - a[i - 1][0]) * y + (a[i][0] + b[0]) * y) % mod
                    heappop(b)

            else:
                ans = (ans + t * (a[i][0] - a[i - 1][0]) * y + x) % mod
        t = z
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)