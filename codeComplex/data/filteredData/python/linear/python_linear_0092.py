def main(n):
    # Generate a deterministic string s of length n over lowercase letters
    # Pattern: repeated 'abcdefghijklmnopqrstuvwxyz'
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = "".join(alphabet[i % 26] for i in range(n))

    # Core logic preserved, with input() removed
    u_set = set()
    for ch in s:
        u_set.add(ch)
    u_cnt = len(u_set)

    d = {}
    j = 0
    ans = 10**9
    for i in range(n):
        while len(d.keys()) < u_cnt and j < n:
            d[s[j]] = d.get(s[j], 0) + 1
            j += 1

        if len(d.keys()) == u_cnt:
            if j - i < ans:
                ans = j - i
        elif j == n:
            break

        d[s[i]] -= 1
        if d[s[i]] == 0:
            del d[s[i]]

    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)