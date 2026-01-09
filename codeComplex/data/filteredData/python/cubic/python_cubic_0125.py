def main(n):
    # Deterministically generate T, and T pairs of strings (s, t) based on n
    # Interpretation: n controls both T and the lengths of s and t
    if n <= 0:
        return

    T = n  # number of test cases
    base_len = max(1, n // 2)

    test_cases = []
    for ti in range(T):
        len_s = base_len + (ti % 5)
        len_t = base_len // 2 + (ti % 3) + 1

        # Generate s and t using a simple deterministic pattern over lowercase letters
        s = ''.join(chr(ord('a') + ((ti * 7 + i * 3) % 26)) for i in range(len_s))
        t = ''.join(chr(ord('a') + ((ti * 11 + i * 5) % 26)) for i in range(len_t))

        test_cases.append((s, t))

    for ti in range(T):
        s, t = test_cases[ti]
        N = len(t)
        for i in range(1, N + 1):
            dp = [0] + [-1] * i
            for l, c in enumerate(s):
                for j in range(i, -1, -1):
                    tmp = dp[j]
                    if dp[j] != -1 and i + dp[j] < N and t[i + dp[j]] == c:
                        tmp = dp[j] + 1
                    if j != 0 and t[j - 1] == c:
                        if dp[j - 1] > tmp:
                            tmp = dp[j - 1]
                    dp[j] = tmp
            if dp[i] == N - i:
                # print("YES")
                pass
                break

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    main(10)