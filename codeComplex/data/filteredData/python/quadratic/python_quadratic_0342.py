def main(n):
    from collections import Counter

    if n <= 0:
        print(-1)
        return

    # 构造长度为 n 的字符串 s 和 t，保证为互为重排
    # s: 0..n-1 映射到 'a'..'z'
    s = [chr(ord('a') + (i % 26)) for i in range(n)]

    # t: 对 s 做一个确定性的排列变换
    # 规则：索引 i 映射到 (i * 2 + 1) % n（当 n > 1），n == 1 时保持不变
    if n == 1:
        t = s[:]
    else:
        t = [None] * n
        for i in range(n):
            j = (i * 2 + 1) % n
            t[i] = s[j]

    cs = Counter(s)
    ct = Counter(t)
    if cs != ct:
        print(-1)
        return

    xs = [[] for _ in range(26)]
    xt = [[] for _ in range(26)]
    for i in range(n):
        j = ord(s[i]) - ord('a')
        xs[j].append(i)

    for i in range(n):
        j = ord(t[i]) - ord('a')
        xt[j].append(i)

    x = [-1] * n
    for i in range(26):
        for j, k in zip(xs[i], xt[i]):
            x[j] = k

    ans = []
    for i in range(n):
        for j in reversed(range(i + 1, n)):
            if x[j - 1] > x[j]:
                x[j - 1], x[j] = x[j], x[j - 1]
                ans.append(j)
    print(len(ans))
    if ans:
        print(*ans)


if __name__ == "__main__":
    main(10)