def main(n):
    # Deterministic generation of a, b from n
    # Ensure a, b >= 1 and sometimes >1 to exercise all branches
    a = (n % 3) + 1
    b = (n % 2) + 1

    if a > 1 and b > 1:
        return

    if n == 3 and a == 1 and b == 1:
        return

    if n == 2 and a == 1 and b == 1:
        return

    t = [[0 for _ in range(n)] for _ in range(n)]

    comp = max(a, b)

    for i in range(comp - 1, n - 1):
        t[i][i + 1] = 1
        t[i + 1][i] = 1

    if b > 1:
        for i in range(n):
            for j in range(n):
                if i != j:
                    t[i][j] = 1 - t[i][j]

    # Keep output similar to original (for determinism / completeness)
    # print("YES")
    pass
    for i in range(n):
        # print("".join(map(str, t[i])))
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size
    main(5)