def main(n):
    # n 表示字符串长度
    if n <= 0:
        print(0)
        return

    # 确定性生成测试字符串：周期性使用小写字母
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    m = len(alphabet)
    s = "".join(alphabet[i % m] for i in range(n))

    want = len(set(s))
    d = {}
    j = 0
    count = 0
    ans = float("inf")
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 0
            count += 1
        d[s[i]] += 1
        if count == want:
            while d[s[j]] > 1:
                d[s[j]] -= 1
                j += 1
            ans = min(ans, i - j + 1)
    print(ans)


if __name__ == "__main__":
    main(1000)