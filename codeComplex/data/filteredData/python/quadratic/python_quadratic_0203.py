def main(n):
    # Interpret n as matrix dimension: n rows, n columns
    rows = n
    cols = n

    # Deterministic construction of X: X[i][j] is '1' iff (i + j) % 3 == 0
    X = [[('1' if (i + j) % 3 == 0 else '0') for j in range(cols)] for i in range(rows)]

    # Compute column sums
    nums = []
    for i in range(cols):
        t = 0
        for j in range(rows):
            t += int(X[j][i])
        nums.append(t)

    # Core logic from original program
    for i in range(rows):
        ok = True
        for j in range(cols):
            if X[i][j] == '1':
                if nums[j] > 1:
                    continue
                else:
                    ok = False
        if ok is True:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    main(5)