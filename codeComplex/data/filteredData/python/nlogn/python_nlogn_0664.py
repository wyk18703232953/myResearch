import random

MOD = 998244353

def merge(a, b):
    inda = 0
    indb = 0
    lena = len(a)
    lenb = len(b)
    d = [a[-1] + b[-1] + 1000]
    a = a + d
    b = b + d
    c = []
    inversions = 0
    for _ in range(lena + lenb):
        if a[inda] < b[indb]:
            c.append(a[inda])
            inda += 1
        else:
            c.append(b[indb])
            indb += 1
            inversions += lena - inda
    return c, inversions

def mergesort(a):
    if len(a) <= 1:
        return a, 0
    split = len(a) // 2
    b = a[:split]
    c = a[split:]
    d, invd = mergesort(b)
    e, inve = mergesort(c)
    f, invf = merge(d, e)
    return f, invf + invd + inve

def main(n):
    # 生成测试数据：长度为 n 的数组 a，元素为 -1 或 1..n
    # 保证非 -1 的值在 1..n 之间
    a = []
    for _ in range(n):
        if random.random() < 0.5:
            a.append(-1)
        else:
            a.append(random.randint(1, n))

    b = []
    for guy in a:
        if guy != -1:
            b.append(guy)

    invs = mergesort(b)[1]
    negs = len(a) - len(b)
    pairs = (negs * (negs - 1)) // 2

    used = [0] * n
    for guy in a:
        if guy != -1:
            used[guy - 1] += 1

    unused = [0]
    for i in range(n - 1):
        unused.append(unused[-1] + 1 - used[i])

    negsseen = 0
    mix = 0
    for i in range(n):
        if a[i] == -1:
            negsseen += 1
        else:
            mix += unused[a[i] - 1] * (negs - negsseen) + negsseen * (negs - unused[a[i] - 1])

    num = invs * 2 * negs + pairs * negs + mix * 2
    denom = 2 * negs

    if negs == 0:
        result = invs % MOD
    else:
        # 直接用扩展欧几里得算法求逆元
        def egcd(a, b):
            if b == 0:
                return a, 1, 0
            g, x, y = egcd(b, a % b)
            return g, y, x - (a // b) * y

        g, x, _ = egcd(denom, MOD)
        # 题目原程序只在 (MOD*i+1) 可被 denom 整除时使用该值，所以相当于 denom | (MOD*i+1)
        # 这里直接按一般意义求 denom 在 MOD 下的逆；若 gcd!=1 会有问题，但保持逻辑简单。
        if g != 1:
            # 若无逆元，则退回原始循环（和原代码逻辑等价）
            for i in range(denom):
                if (MOD * i + 1) % denom == 0:
                    inv = (MOD * i + 1) // denom
                    break
        else:
            inv = x % MOD

        result = (num * inv) % MOD

    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)