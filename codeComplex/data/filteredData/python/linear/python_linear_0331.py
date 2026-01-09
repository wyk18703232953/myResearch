def main(n):
    # Interpret n as the number of points between 0 and M.
    # Deterministically generate A and M.
    # Example: A = [1, 3, 6, 10, ...] (prefix sums of 1..n), M = last A + 5
    if n <= 0:
        # print(0)
        pass
        return

    A = [i * (i + 1) // 2 for i in range(1, n + 1)]
    M = A[-1] + 5

    A = [0] + A + [M]
    D = []
    for i in range(n + 1):
        D.append(A[i + 1] - A[i])

    E = []
    O = []
    for i, d in enumerate(D):
        if i % 2 == 0:
            E.append(d)
            O.append(0)

        else:
            O.append(d)
            E.append(0)

    from itertools import accumulate
    CE = [0] + E
    CE = list(accumulate(CE))
    CO = [0] + O
    CO = list(accumulate(CO))

    ans = CE[-1]
    for i in range(n + 1):
        if D[i] == 1:
            continue
        temp = CE[i] + (D[i] - 1) + CO[-1] - CO[i + 1]
        ans = max(ans, temp)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)