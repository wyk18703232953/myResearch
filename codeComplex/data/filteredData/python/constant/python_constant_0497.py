def main(n):
    # n: number of test cases
    q = n
    otvet = []
    for i in range(q):
        # Deterministic generation of (n, m, k) for each test case
        # Use different patterns to cover various branches
        ni = i - n // 2
        mi = (2 * i - n) // 3
        ki = n + (i % 5)

        # Core logic from original program
        if ni < 0:
            ni = -ni
        if mi < 0:
            mi = -mi
        if mi > ki or ni > ki:
            otvet.append(-1)
        elif mi % 2 == ki % 2 and ni % 2 == ki % 2:
            otvet.append(ki)
        elif mi % 2 == ki % 2 or ni % 2 == ki % 2:
            otvet.append(ki - 1)

        else:
            otvet.append(ki - 2)

    for x in otvet:
        # print(x)
        pass
if __name__ == "__main__":
    main(10)