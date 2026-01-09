def main(n):
    # Interpret n as both the number of rows and columns
    rows = n
    cols = n

    # Deterministically generate X: matrix of '0'/'1' chars
    # Example pattern: X[i][j] = '1' if (i + j) % 3 != 0 else '0'
    X = []
    for i in range(rows):
        row = [('1' if (i + j) % 3 != 0 else '0') for j in range(cols)]
        X.append(row)

    # Core logic from original code
    nums = []
    for i in range(cols):
        t = 0
        for j in range(rows):
            t += int(X[j][i])
        nums.append(t)

    for i in range(rows):
        ok = True
        for j in range(cols):
            if X[i][j] == '1':
                if nums[j] > 1:
                    continue

                else:
                    ok = False
        if ok is True:
            # print("YES")
            pass
            return
    # print("NO")
    pass
if __name__ == "__main__":
    main(10)