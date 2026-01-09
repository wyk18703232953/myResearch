def main(n):
    # n controls the length of the base string s, k is fixed
    k = 3
    if n <= 0:
        return ""
    # Deterministically generate s as a repeating pattern of lowercase letters
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = "".join(alphabet[i % 26] for i in range(n))

    flag = True
    lenn = 10 ** 18
    ans = ""

    for i in range(n):
        s1 = s + s[n - i - 1:] * (k - 1)
        cnt = 0
        L = len(s)
        for j in range(len(s1) - L + 1):
            if s1[j:j + L] == s:
                cnt += 1
        if cnt == k and len(s1) < lenn:
            ans = s1
            lenn = len(s1)
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    main(5)