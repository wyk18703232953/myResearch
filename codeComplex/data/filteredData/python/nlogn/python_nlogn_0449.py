def main(n):
    # Interpret n as the length of the array s
    # Construct a deterministic m and s
    if n <= 0:
        return 0

    # Deterministic choice of m based on n
    # Ensure m exists in s by setting one position explicitly to m
    m = (n // 3) + 1  # some positive value depending on n

    # Construct s of length n, deterministic pattern with values around m
    s = []
    for i in range(n):
        if i == n // 2:
            # Guarantee at least one occurrence of m
            s.append(m)
        else:
            # Deterministically distribute values smaller, equal and larger than m
            # Use a simple arithmetic pattern around m
            if i % 3 == 0:
                s.append(m - 1 if m - 1 > 0 else m)
            elif i % 3 == 1:
                s.append(m + 1)
            else:
                s.append(m + (i // 3) % 5)

    # Core logic from original code, without I/O side-effects
    try:
        ind = s.index(m)
    except ValueError:
        return 0

    dp = [0 for _ in range(n)]
    for i in range(ind + 1, n):
        if s[i] < m:
            dp[i] = dp[i - 1] - 1
        elif s[i] > m:
            dp[i] = dp[i - 1] + 1

    for i in range(ind - 1, -1, -1):
        if s[i] < m:
            dp[i] = dp[i + 1] - 1
        elif s[i] > m:
            dp[i] = dp[i + 1] + 1

    d = {}
    for i in range(ind + 1, n):
        key = dp[i]
        if key in d:
            d[key] += 1
        else:
            d[key] = 1

    ans = 0
    for i in range(ind + 1):
        x = -dp[i]
        if x in d:
            ans += d[x]
        if (x + 1) in d:
            ans += d[x + 1]
        if dp[i] == 0 or dp[i] == 1:
            ans += 1

    return ans


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    result = main(10)
    print(result)