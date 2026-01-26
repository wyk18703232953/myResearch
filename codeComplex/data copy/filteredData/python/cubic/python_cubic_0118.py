#!/usr/bin/env python3

def solve_single_case(s, t):
    ok = False
    for i in range(len(t)):
        t1 = list(t[:i]) + ["#"]
        t2 = list(t[i:]) + ["#"]
        dp = [[-1] * (len(t) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = 0
        for j, ch in enumerate(s):
            for k in range(len(t1)):
                if dp[j][k] == -1:
                    continue
                if dp[j+1][k] < dp[j][k]:
                    dp[j+1][k] = dp[j][k]
                if ch == t1[k]:
                    if dp[j+1][k+1] < dp[j][k]:
                        dp[j+1][k+1] = dp[j][k]
                back_index = dp[j][k]
                if back_index < len(t2) and ch == t2[back_index]:
                    if dp[j+1][k] < dp[j][k] + 1:
                        dp[j+1][k] = dp[j][k] + 1
        for k in range(len(t) + 1):
            if dp[len(s)][k] + k >= len(t):
                ok = True
                break
        if ok:
            break
    return "YES" if ok else "NO"


def generate_test_case(case_index, n):
    # Deterministically generate s and t based on n and case_index
    # Let |t| = max(1, n // 2), |s| = n
    if n <= 0:
        return "a", "a"
    len_t = max(1, n // 2)
    len_s = n

    alphabet = ["a", "b", "c"]

    def char_from_idx(idx):
        return alphabet[(idx + case_index) % len(alphabet)]

    s = [char_from_idx(i) for i in range(len_s)]
    t = [alphabet[(i * 2 + case_index) % len(alphabet)] for i in range(len_t)]
    return "".join(s), "".join(t)


def main(n):
    t_cases = max(1, n)
    results = []
    for case_index in range(t_cases):
        s, t_str = generate_test_case(case_index, n)
        res = solve_single_case(list(s), t_str)
        results.append(res)
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)