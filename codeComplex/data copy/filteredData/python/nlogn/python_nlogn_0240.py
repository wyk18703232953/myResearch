def main(n):
    p = [[i, (i * 2) % (n + 1)] for i in range(n)]

    f = lambda a, b, c: (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    def g(fi, se, p_list):
        q = []
        for x in p_list:
            if f(fi, se, x):
                if len(q) < 2:
                    q.append(x)

                else:
                    if f(q[0], q[1], x):
                        return 1
        return 0

    if n > 4 and all([g(p[0], p[1], p), g(p[0], p[2], p), g(p[1], p[2], p)]):
        return "NO"

    else:
        return "YES"


if __name__ == "__main__":
    # print(main(10))
    pass