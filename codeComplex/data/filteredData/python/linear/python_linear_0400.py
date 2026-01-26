def main(n):
    # Deterministic generation of input based on n
    # n is the number of stages
    if n <= 0:
        return

    m = n * 10.0
    up = [2 + (i % 9) for i in range(n)]
    down = [2 + ((i * 3) % 9) for i in range(n)]

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
        # print("{:.10f}".format(l))
        pass
if __name__ == "__main__":
    main(5)