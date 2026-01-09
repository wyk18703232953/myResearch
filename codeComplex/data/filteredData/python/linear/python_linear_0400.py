def main(n):
    # Map n to problem parameters deterministically
    # n: number of segments
    # m: base weight
    # up[i], down[i] are generated deterministically based on i and n

    if n <= 0:
        n = 1

    m = n * 10

    up = [2 + (i % 5) for i in range(n)]
    down = [2 + ((i * 3) % 7) for i in range(n)]

    def check(x):
        weight = m + x
        fuel = x
        for i in range(n):
            f = weight / up[i]
            if fuel < f:
                return False
            weight -= f
            fuel -= f
            f = weight / down[i]
            if fuel < f:
                return False
            weight -= f
            fuel -= f
        return True

    l = 0.0
    r = 1e9 + 1e-6

    for _ in range(100):
        mid = (r + l) / 2.0
        if check(mid):
            r = mid

        else:
            l = mid
        if r - l <= 1e-10:
            break

    if l >= 1e9 + 1e-6:
        # print(-1)
        pass

    else:
        # print(f"{l:.10f}")
        pass
if __name__ == "__main__":
    main(10)