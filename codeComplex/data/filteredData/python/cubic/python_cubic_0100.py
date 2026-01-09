d = {i: 2 ** i for i in range(10)}

MOD = 998244353


def can(i, m):
    return d[i] & m


def calc(m):
    b = 1
    c = 0
    for _ in range(10):
        if b & m:
            c += 1
        b <<= 1
    return c


def sm(ln, k, m, s='', first=False, cache=None):
    if ln < 1:
        return 0, 1

    key = (ln, k, m, s, first)
    if key in cache:
        return cache[key]

    ans = 0
    count = 0
    base = 10 ** (ln - 1)

    use_new = calc(m) < k

    if s:
        finish = int(s[0]) + 1

    else:
        finish = 10

    for i in range(finish):
        if use_new or can(i, m):
            ss = s[1:]
            if i != finish - 1:
                ss = ''
            nm = m | d[i]
            nfirst = False
            if i == 0 and first:
                nm = m
                nfirst = True
            nexta, nextc = sm(ln - 1, k, nm, ss, nfirst, cache)
            ans += base * i * nextc + nexta
            count += nextc

    cache[key] = (ans, count)
    return ans, count


def call(a, k, cache):
    s = str(a)
    return sm(len(s), k, 0, s, True, cache)[0]


def main(n):
    # 根据规模 n 生成测试数据：
    # 令区间长度约为 n，k 在 [1, 10] 内循环取值
    l = 1
    r = max(1, n)
    k = (n % 10) + 1

    cache = {}
    res = (call(r, k, cache) - call(l - 1, k, cache)) % MOD
    # print(res)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 100 运行
    main(100)