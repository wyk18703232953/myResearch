import math

def calc(st, j):
    ans = 9999999999999999999999
    if j >= len(st):
        return 0
    j = len(st) - j
    for i in range(j - 1, len(st)):
        ans = min(ans, st[i] - st[i - j + 1] + 1)
    return ans

def run_algorithm(n, m, k, s):
    inf = 99999999999999999999
    dp = [[inf for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(k + 1):
        dp[0][i] = 0
    for i in range(1, n + 1):
        st = []
        for ik in range(len(s[i - 1])):
            if s[i - 1][ik] == '1':
                st.append(ik)
        for j in range(k + 1):
            no = calc(st, j)
            for t in range(k + 1 - j):
                dp[i][t + j] = min(dp[i][t + j], no + dp[i - 1][t])
    return dp[n][k]

def generate_input(n):
    # Interpret n as both number of rows and row length
    if n <= 0:
        n_rows = 1
        m = 1

    else:
        n_rows = n
        m = n
    # Set k proportional to m but not exceeding total possible '1's
    # Here choose k = m // 2 for determinism
    k = m // 2
    # Deterministically generate n_rows binary strings of length m
    # Pattern: s[i][j] = '1' if (i * 131 + j * 17) % 3 == 0 else '0'
    s = []
    for i in range(n_rows):
        row = ['0'] * m
        base = i * 131
        for j in range(m):
            if (base + j * 17) % 3 == 0:
                row[j] = '1'
        s.append(''.join(row))
    return n_rows, m, k, s

def main(n):
    n_rows, m, k, s = generate_input(n)
    result = run_algorithm(n_rows, m, k, s)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)