def main(n):
    # Interpret n as the length of the string s, k = n // 2 (at least 1)
    if n <= 0:
        return
    k = max(1, n // 2)

    # Deterministically generate a string s of length n over 'R', 'G', 'B'
    chars = ['R', 'G', 'B']
    s = ''.join(chars[i % 3] for i in range(n))

    a = 10**9
    ans = [[0] * n for _ in range(3)]
    curr = ['R', 'G', 'B']

    # Precompute mismatch arrays for three starting phases
    for l in range(3):
        z = l
        for j in range(n):
            if s[j] != curr[z]:
                ans[l][j] = 1
            z += 1
            z %= 3

    # Convert to 1-based prefix sums
    for i in range(3):
        ans[i] = [0] + ans[i]

    for l in range(3):
        for j in range(1, n + 1):
            ans[l][j] += ans[l][j - 1]

    # Slide window of length k
    for l in range(3):
        for j in range(1, n - k + 2):
            a = min(a, ans[l][j + k - 1] - ans[l][j - 1])

    # print(a)
    pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10**5)