def main(n):
    # n: number of internal points; we deterministically build A and M from n
    # Construct a simple increasing sequence A of length n:
    # A[i] = 2 * (i + 1), so gaps are fixed and deterministic
    A = [2 * (i + 1) for i in range(n)]
    # Let M be the last A plus 2, so there is always a tail segment
    M = (2 * n + 2) if n > 0 else 2

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
    return ans


if __name__ == "__main__":
    # Example deterministic calls for time-complexity experiments
    for size in [1, 2, 5, 10, 20]:
        # print(size, main(size))
        pass