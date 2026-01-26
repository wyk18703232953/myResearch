def main(n):
    # n: number of input numbers (scale parameter)
    # Deterministic generation of inputs: x_i = i * (i + 1)
    t = [0 for _ in range(2000)]
    c = [0 for _ in range(2000)]
    for i in range(n):
        x = i * (i + 1)
        r = 0
        ok = False
        for j in range(2000):
            if x >> j & 1:
                if t[j] != 0:
                    x ^= t[j]
                    r ^= c[j]
                else:
                    t[j] = x
                    c[j] = r ^ (1 << i)
                    ok = True
                    break
        if ok:
            print(0)
            continue
        a = []
        for j in range(2000):
            if r >> j & 1:
                a.append(j)
        print(len(a))
        for y in a:
            print(y)


if __name__ == "__main__":
    main(10)