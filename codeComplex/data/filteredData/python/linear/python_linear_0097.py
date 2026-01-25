def main(n):
    # 构造确定性字符串 s，长度为 n
    # 使用重复的模式 'abcde' 来保证有多个不同字符
    base = "abcde"
    if n <= 0:
        print(0)
        return
    s = (base * (n // len(base) + 1))[:n]

    p, q, r = len(set(s)), {}, 10**6
    for i in range(n):
        q[s[i]] = i
        if len(q) == p:
            r = min(r, max(q.values()) - min(q.values()))
    print(r + 1)


if __name__ == "__main__":
    main(10)