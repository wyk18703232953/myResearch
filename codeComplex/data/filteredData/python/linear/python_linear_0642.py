def main(n):
    # Deterministic generation of A with length n and sum(A) >= 2*n-2 when n > 1
    if n <= 0:
        return
    if n == 1:
        A = [1]
    else:
        A = [2] * n
        need = 2 * n - 2
        s = sum(A)
        i = 0
        # Reduce some positions from 2 to 1 to adjust the sum exactly to need
        while s > need and i < n:
            A[i] = 1
            s -= 1
            i += 1

    if sum(A) < 2 * n - 2:
        print("NO")
        return

    ONES = A.count(1)
    print("YES", min(n - 1, n - ONES + 1))

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

    print(len(ANS))
    for a, b in ANS:
        print(a, b)


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)