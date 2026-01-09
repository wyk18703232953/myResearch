def main(n):
    A = list(range(1, n + 1))
    B = [((i * 2) % n) + 1 for i in range(n)]

    REVA = [None] * (n + 1)
    for i in range(n):
        REVA[A[i]] = i + 1

    top = 0
    ANSLIST = []
    for b in B:
        if REVA[b] > top:
            ANSLIST.append(REVA[b] - top)
            top = REVA[b]

        else:
            ANSLIST.append(0)

    for ans in ANSLIST:
        # print(ans, end=" ")
        pass
if __name__ == "__main__":
    main(10)