def main(n):
    # Interpret n as: number of rows = n, number of columns = n, k = n//2
    rows = n
    cols = n
    k = n // 2

    # Deterministically generate a binary matrix of size rows x cols
    # Pattern: cell (i,j) = '1' if (i + j) % 3 == 0 else '0'
    matrix = []
    for i in range(rows):
        row = [('1' if (i + j) % 3 == 0 else '0') for j in range(cols)]
        matrix.append(row)

    dp = [0] * (k + 1)
    l = []
    fk = None

    for r in range(rows):
        s = matrix[r]
        d = []
        if list(set(s)) == ['0']:
            d.append(0)
            continue
        one = []
        for i in range(len(s)):
            if s[i] == '1':
                one.append(i)
        ni = len(one)
        d = [1e9] * (ni + 1)
        d[-1] = 0
        for i in range(ni):
            for j in range(i, ni):
                d[ni - (j - i + 1)] = min(d[ni - (j - i + 1)], one[j] - one[i] + 1)
        l.append(d)
        fk = [1e9] * (k + 1)
        for i in range(k + 1):
            for j in range(ni + 1):
                if i + j > k:
                    break
                fk[i + j] = min(fk[i + j], dp[i] + d[j])
        dp = fk[:]

    result = min(dp)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(300)