MOD = 1000000007

def add(a, b):
    return (a + b) % MOD

def mul(a, b):
    return (a * b) % MOD

def sub(a, b):
    return (a - b + MOD) % MOD

def qpow(a, b):
    r = 1
    k = a
    # 原代码固定17位，这里保持一致
    for i in range(17):
        if b & (1 << i):
            r = mul(r, k)
        k = mul(k, k)
    return r

def main(n):
    # 生成长度为 n 的二进制串 a（这里简单生成全 1 串）
    a = ['1'] * n

    # 生成查询数 q，并构造 q 个区间查询
    # 为了有一定规模，这里设 q = n，并让区间分布在 [1, n]
    q = n

    # 构造前缀和数组 c，c[i] 为前 i 个字符为 '1' 的个数
    c = [0] * (n + 1)
    for i in range(n):
        c[i + 1] = c[i] + int(a[i])

    # 构造并处理 q 个查询
    # 这里示例：第 i 个查询区间为 [1, i]（i 从 1 到 q，且 q <= n）
    for i in range(1, q + 1):
        l, r = 1, i
        k = (r - l + 1)
        o = c[r] - c[l - 1]
        z = sub(qpow(2, o), 1)
        print(mul(z, qpow(2, k - o)))

if __name__ == "__main__":
    # 示例调用：n = 10
    main(10)