def main(n):
    # Deterministically generate input data A of size n
    # Permutation of 1..n using a simple reversible pattern
    if n <= 0:
        # print("")
        pass
        return

    A = [(i * 2 + 1) % n + 1 for i in range(n)]

    PLACE = [None] * (n + 1)
    for i in range(n):
        PLACE[A[i]] = i

    al = n
    WINLIST = [None] * (n + 1)  # 0: lose, 1: win; here use "A"/"B" as in original

    def move(x, al):
        place = PLACE[x]
        for i in range(place, -1, -x):
            if A[i] > x and WINLIST[A[i]] == "B":
                WINLIST[x] = "A"
                return
        for i in range(place, al, x):
            if A[i] > x and WINLIST[A[i]] == "B":
                WINLIST[x] = "A"
                return
        WINLIST[x] = "B"
        return

    for j in range(n, 0, -1):
        move(j, al)

    ANS = ""
    for i in A:
        ANS += WINLIST[i]

    # print(ANS)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)