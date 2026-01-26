def main(n):
    # Deterministically generate input: list of (x, w)
    # Here we choose:
    # x = i
    # w = 1 + (i % 5)
    xw = [[i, 1 + (i % 5)] for i in range(n)]

    ab = sorted([[x - w, x + w] for x, w in xw], key=lambda x: (x[1], x[0]))

    if not ab:
        # print(0)
        pass
        return

    k = ab[0][0]
    cnt = 0
    for a, b in ab:
        if k <= a:
            cnt += 1
            k = b

    # print(cnt)
    pass
if __name__ == "__main__":
    main(10)