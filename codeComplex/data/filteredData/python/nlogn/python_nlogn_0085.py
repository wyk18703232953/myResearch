def main(n):
    # n: number of participants
    # deterministically construct k and tm list

    if n <= 0:
        return

    # choose k in [1, n] deterministically
    k = n // 2 + 1

    tm = []
    for i in range(n):
        # deterministic generation of (p, t)
        p = (i % 5) + 1          # scores in [1, 5]
        t = (i // 5) + 1         # time increases in blocks of 5
        tm.append([p, t])

    tm.sort(key=lambda x: (-x[0], x[1]))
    ans = tm.count(tm[k - 1])
    # print(ans)
    pass
if __name__ == "__main__":
    # example call with a chosen scale
    main(10)