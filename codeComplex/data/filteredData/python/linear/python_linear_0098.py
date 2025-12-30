import random
import string

def bs(l, h, gf):
    while l < h:
        m = (l + h) // 2
        if gf(m):
            h = m
        else:
            l = m + 1
    return l

def make_gf(s, u, n):
    # 生成闭包，保持与原 gf 行为一致
    def gf(x):
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
    return gf

def main(n: int):
    # 根据 n 生成测试数据：长度为 n 的随机小写字符串
    # 保证字符串非空时至少包含 1 个不同字符的集合
    alphabet_size = min(5, max(1, n))  # 控制字符种类数量，最多 5 种
    alphabet = string.ascii_lowercase[:alphabet_size]
    s = ''.join(random.choice(alphabet) for _ in range(n))

    u = set(s)
    gf = make_gf(s, u, n)
    ans = bs(1, n, gf)
    print(ans)

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)