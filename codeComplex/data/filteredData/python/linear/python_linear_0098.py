def bs(l, h, n, s, u):
    while l < h:
        m = (l + h) // 2
        if gf(m, n, s, u):
            h = m

        else:
            l = m + 1
    return l

def gf(x, n, s, u):
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
    # 生成一个确定性的字符串 s，长度为 n
    # 使用小写字母周期性构造
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = "".join(alphabet[i % len(alphabet)] for i in range(n))
    u = set(s)
    result = bs(1, n, n, s, u)
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)