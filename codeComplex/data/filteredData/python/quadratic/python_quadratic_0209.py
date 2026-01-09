def main(n):
    # Interpret n as both the number of rows and the length of each binary string
    m = n
    if n <= 0:
        # print("NO")
        pass
        return

    # Deterministically generate n binary strings of length m
    # Pattern: for i-th row, j-th bit is (i + j) % 2
    A = ["".join(str((i + j) % 2) for j in range(m)) for i in range(n)]

    C = [0] * m
    for i in range(n):
        a = A[i]
        for j, c in enumerate(a):
            C[j] += int(c)

    for i in range(n):
        a = A[i]
        for j, c in enumerate(a):
            C[j] -= int(c)
        for j in range(m):
            if C[j] == 0:
                break

        else:
            # print("YES")
            pass
            return
        for j, c in enumerate(a):
            C[j] += int(c)
    # print("NO")
    pass
if __name__ == "__main__":
    # Example deterministic call; change 10 to other n for scaling experiments
    main(10)