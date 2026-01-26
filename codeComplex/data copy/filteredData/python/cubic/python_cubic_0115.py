INF = 1e20


def solve(s1, s2, next_pos):
    dp = [[INF for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    dp[0][0] = 0
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if dp[i][j] == INF:
                continue
            if i < len(s1) and dp[i][j] < len(next_pos) and next_pos[int(dp[i][j])][ord(s1[i]) - ord('a')] < INF:
                dp[i + 1][j] = min(dp[i + 1][j], next_pos[int(dp[i][j])][ord(s1[i]) - ord('a')] + 1)
            if j < len(s2) and dp[i][j] < len(next_pos) and next_pos[int(dp[i][j])][ord(s2[j]) - ord('a')] < INF:
                dp[i][j + 1] = min(dp[i][j + 1], next_pos[int(dp[i][j])][ord(s2[j]) - ord('a')] + 1)
    return dp[len(s1)][len(s2)]


def process_case(s, rs):
    next_pos = [[INF for _ in range(26)] for _ in range(len(s))]
    for i in range(len(s) - 1, -1, -1):
        if i < len(s) - 1:
            for j in range(26):
                next_pos[i][j] = next_pos[i + 1][j]
        next_pos[i][ord(s[i]) - ord('a')] = i

    found = False
    if len(rs) == 1:
        if rs in s:
            found = True

    else:
        for p in range(1, len(rs)):
            s1 = rs[:p]
            s2 = rs[p:]
            if solve(s1, s2, next_pos) < INF:
                found = True
                break
    return found


def main(n):
    results = []
    T = max(1, n)
    base_len = max(1, n)
    for t in range(T):
        Ls = base_len + (t % 3)
        Lr = max(1, base_len // 2 + (t % 5))
        s = ''.join(chr(ord('a') + ((i + t) % 26)) for i in range(Ls))
        rs = ''.join(chr(ord('a') + ((2 * i + t) % 26)) for i in range(Lr))
        found = process_case(s, rs)
        results.append('YES' if found else 'NO')
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)