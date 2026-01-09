def main(n):
    # Map n to original parameters:
    # n_rows = n, m = n (columns), k = n (max removals)
    # This keeps input size roughly O(n^2) characters.
    n_rows = n
    m = n
    k = n

    # Deterministic generation of table: pattern based on indices
    table = []
    for r in range(n_rows):
        row_chars = []
        for c in range(m):
            # Simple deterministic pattern: '1' if (r + c) % 3 == 0, else '0'
            if (r + c) % 3 == 0:
                row_chars.append('1')

            else:
                row_chars.append('0')
        table.append(''.join(row_chars))

    dp = [0] * (k + 1)

    for a in table:
        one = []
        for i in range(m):
            if a[i] == '1':
                one.append(i)

        if not one:
            continue

        ni = len(one)
        subdp = [10 ** 9] * (ni + 1)
        subdp[-1] = 0

        for i in range(ni):
            for j in range(i, ni):
                length = j - i + 1
                index = ni - length
                cost = one[j] - one[i] + 1
                if cost < subdp[index]:
                    subdp[index] = cost

        next_dp = [10 ** 9] * (k + 1)
        for i in range(k, -1, -1):
            base = dp[i]
            for j in range(ni + 1):
                if i + j > k:
                    break
                val = base + subdp[j]
                if val < next_dp[i + j]:
                    next_dp[i + j] = val
        dp = next_dp

    result = min(dp)
    # print(result)
    pass
if __name__ == "__main__":
    main(200)