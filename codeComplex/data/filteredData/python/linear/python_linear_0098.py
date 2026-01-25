def bs(l, h, s, u, n):
    while l < h:
        m = (l + h) // 2
        if gf(m, s, u, n):
            h = m
        else:
            l = m + 1
    return l

def gf(x, s, u, n):
    d = {}
    for i in range(x):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    if len(d) == len(u):
        return 1
    for i in range(x, n):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
        d[s[i - x]] -= 1
        if not d[s[i - x]]:
            del d[s[i - x]]
        if len(d) == len(u):
            return 1
    return 0

def main(n):
    if n <= 0:
        print(0)
        return
    # 构造确定性字符串：在前 min(n, 26) 个位置循环使用小写字母
    # 当 n>26 时，字符会重复，但集合大小固定为 26
    base = "abcdefghijklmnopqrstuvwxyz"
    s = "".join(base[i % len(base)] for i in range(n))
    u = set(s)
    ans = bs(1, n, s, u, n)
    print(ans)

if __name__ == "__main__":
    main(10)