def main(n):
    # n 表示字符串长度
    if n <= 0:
        # print(0)
        pass
        return

    # 构造一个确定性的字符串 S，包含多个不同字符，长度为 n
    # 使用周期性模式保证有重复和多种字符
    base_chars = "abcde"
    m = len(base_chars)
    S = "".join(base_chars[i % m] for i in range(n))

    M = {}
    N = len(S)

    s = set()
    for c in S:
        s.add(c)
        M[c] = 0

    i = 0
    j = -1
    aux = 0
    ans = 10 ** 18

    while j < N - 1:
        j += 1
        M[S[j]] += 1
        if M[S[j]] == 1:
            aux += 1
        while M[S[i]] > 1:
            M[S[i]] -= 1
            i += 1
        if aux == len(s):
            ans = min(ans, j - i + 1)

    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)