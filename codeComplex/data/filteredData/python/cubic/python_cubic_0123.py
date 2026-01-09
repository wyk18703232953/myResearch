def find_it(s, left, right, nxt):
    dp = [[1000 for _ in range(len(right) + 1)] for _ in range(len(left) + 1)]
    dp[0][0] = 0
    for i in range(len(left) + 1):
        for j in range(len(right) + 1):
            if dp[i][j] > len(s):
                continue
            if j < len(right) and nxt[ord(right[j]) - 97][dp[i][j]] != -1:
                if nxt[ord(right[j]) - 97][dp[i][j]] < dp[i][j + 1]:
                    dp[i][j + 1] = nxt[ord(right[j]) - 97][dp[i][j]] + 1
            if i < len(left) and nxt[ord(left[i]) - 97][dp[i][j]] != -1:
                if nxt[ord(left[i]) - 97][dp[i][j]] < dp[i + 1][j]:
                    dp[i + 1][j] = nxt[ord(left[i]) - 97][dp[i][j]] + 1
    return dp[len(left)][len(right)] != 1000

def process_case(s, t):
    nxt = [[-1 for _ in range(len(s) + 1)] for _ in range(26)]
    for i, x in enumerate(s):
        nxt[ord(x) - 97][i] = i
    for i in range(26):
        for j in range(len(s) - 1, -1, -1):
            if nxt[i][j] != j:
                nxt[i][j] = nxt[i][j + 1]
    r = False
    for i in range(len(t)):
        res = find_it(s, t[:i], t[-len(t) + i:], nxt)
        if res:
            r = True
            break
    return "YES" if r else "NO"

def main(n):
    results = []
    # Interpret n as: number of test cases = n
    # For test case i (0-based):
    #   |s| = i + 1
    #   |t| = i + 1
    # Strings are deterministic over 'a'..'z' using modular patterns.
    for i in range(n):
        length_s = i + 1
        length_t = i + 1
        s = "".join(chr(97 + (j % 26)) for j in range(length_s))
        t = "".join(chr(97 + ((j * 2) % 26)) for j in range(length_t))
        results.append(process_case(s, t))
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(5)