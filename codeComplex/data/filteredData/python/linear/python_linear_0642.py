def main(n):
    # Deterministic generation of A with length n
    # Pattern: values cycle through 1,2,3 to ensure mixture and sum >= 2n-2 for most n
    A = [(i % 3) + 1 for i in range(n)]

    # Core logic from original program (with input/output removed except prints)
    if sum(A) < 2 * n - 2:
        # print("NO")
        pass
        return

    ONES = A.count(1)
    # print("YES", min(n - 1, n - ONES + 1))
    pass

    NOONE = []
    for i in range(n):
        if A[i] != 1:
            NOONE.append([A[i], i + 1])

    ANS = []
    for i in range(1, len(NOONE)):
        ANS.append((NOONE[i - 1][1], NOONE[i][1]))
        NOONE[i - 1][0] -= 1
        NOONE[i][0] -= 1

    NOONE = [[1, NOONE[-1][1]]] + NOONE[0:-1] + [[NOONE[-1][0] - 1, NOONE[-1][1]]]

    LENNO = len(NOONE)

    j = 0
    for i in range(n):
        while j < LENNO and NOONE[j][0] == 0:
            j += 1
        if A[i] != 1:
            continue
        ANS.append((i + 1, NOONE[j][1]))
        NOONE[j][0] -= 1

    # print(len(ANS))
    pass
    for a, b in ANS:
        # print(a, b)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)