def main(n):
    # n controls both number of test cases and string sizes deterministically
    T = max(1, n // 3)
    base_len_s = max(1, n // 2)
    base_len_t = max(1, n // 3)

    def generate_string(length, offset):
        # deterministic lowercase string based on length and offset
        return "".join(chr(ord("a") + (i + offset) % 26) for i in range(length))

    results = []
    for case in range(T):
        # Vary lengths slightly with case index to make instances distinct but deterministic
        len_s = base_len_s + (case % 5)
        len_t = base_len_t + (2 * case % 7)
        s = generate_string(len_s, case)
        t = generate_string(len_t, case * 3)

        n_s = len(s)

        find = [[n_s] * 26 for _ in range(n_s + 2)]
        for i in range(n_s - 1, -1, -1):
            find[i][:] = find[i + 1]
            find[i][ord(s[i]) - ord("a")] = i

        def interleaving(a, b):
            dp = [n_s] * (len(b) + 1)
            for i in range(len(a) + 1):
                for j in range(len(b) + 1):
                    if i == j == 0:
                        dp[j] = -1
                        continue
                    res = n_s
                    if i > 0:
                        res = min(res, find[dp[j] + 1][ord(a[i - 1]) - ord("a")])
                    if j > 0:
                        res = min(res, find[dp[j - 1] + 1][ord(b[j - 1]) - ord("a")])
                    dp[j] = res
            return dp[-1] < n_s

        if any(interleaving(t[:i], t[i:]) for i in range(len(t))):
            results.append("YES")

        else:
            results.append("NO")

    # Ensure some output to avoid optimization removal in some environments
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)