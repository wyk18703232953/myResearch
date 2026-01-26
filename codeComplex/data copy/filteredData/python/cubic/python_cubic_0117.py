def list2d(a, b, c):
    return [[c] * b for _ in range(a)]

INF = 10 ** 18
MOD = 10 ** 9 + 7

def check(x, S, T, N, M):
    T1 = T[:x] + '*'
    T2 = T[x:] + '*'
    m1 = len(T1)
    m2 = len(T2)

    dp = list2d(N + 1, m1, -1)
    dp[0][0] = 0
    for i in range(N):
        s = S[i]
        for j in range(m1):
            k = dp[i][j]
            if k != -1:
                if dp[i + 1][j] < k:
                    dp[i + 1][j] = k
                if T1[j] == s:
                    if dp[i + 1][j + 1] < k:
                        dp[i + 1][j + 1] = k
                if T2[k] == s:
                    if dp[i + 1][j] < k + 1:
                        dp[i + 1][j] = k + 1
    return dp[N][m1 - 1] == m2 - 1

def generate_test_case(idx, n):
    # Deterministically generate S and T for test case idx, scale with n
    # Let length of S be n + idx, length of T be n//2 + idx//2 (at least 1)
    lenS = n + idx
    lenT = max(1, n // 2 + idx // 2)

    # Build S as repeating lowercase letters pattern
    S = ''.join(chr(ord('a') + (i % 26)) for i in range(lenS))

    # Build T as another deterministic pattern derived from S
    # For diversity, pick characters from S at positions with step based on idx+1
    step = (idx + 1) % lenS or 1
    T_chars = []
    pos = 0
    for _ in range(lenT):
        T_chars.append(S[pos])
        pos = (pos + step) % lenS
    T = ''.join(T_chars)
    return S, T

def main(n):
    # Interpret n as: number of test cases = n,
    # each test case size grows with n for scalability.
    T_cases = max(1, n)

    results = []
    for t in range(T_cases):
        S, T_str = generate_test_case(t, n)
        N = len(S)
        M = len(T_str)
        ok = False
        for x in range(M):
            if check(x, S, T_str, N, M):
                ok = True
                break
        results.append("YES" if ok else "NO")

    # Output results to keep behavior observable
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size
    main(10)