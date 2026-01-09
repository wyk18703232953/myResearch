base = 998244353

def power(x, y):
    if y == 0:
        return 1
    t = power(x, y // 2)
    t = (t * t) % base
    if y % 2:
        t = (t * x) % base
    return t

def inverse(x):
    return power(x, base - 2)

# 预处理阶乘和逆元
MAXN = 6000
f = [1]
iv = [1]
for i in range(1, MAXN):
    f.append((f[i - 1] * i) % base)
    iv.append(inverse(f[i]))

def C(n, k):
    if k < 0 or k > n:
        return 0
    return (f[n] * iv[k] * iv[n - k]) % base

def candy(n, k):
    return C(n + k - 1, k - 1)

def count_game(k, n, x):  # k players, n points total, no player can have x point or more
    if k == 0:
        return 1 if n == 0 else 0
    ans = 0
    for i in range(0, k + 1):
        t = n - x * i
        if t < 0:
            break
        if i % 2:
            ans = (ans - C(k, i) * candy(t, k)) % base

        else:
            ans = (ans + C(k, i) * candy(t, k)) % base
    return ans

def main(n):
    """
    n 为规模参数，用于生成测试数据:
    这里构造:
        p = n % 5 + 2  (玩家数，至少 2)
        r = n % 7 + 1
        s = r + n % 10 + 1 (保证 s >= r + 1)

    返回原程序计算得到的答案。
    """
    p = n % 5 + 2
    r = n % 7 + 1
    s = r + (n % 10) + 1

    gamesize = count_game(p, s - r, int(1e18))
    gamesize = inverse(gamesize)
    ans = 0
    for q in range(r, s + 1):
        for i in range(0, p):  # exactly i people have the same score
            t = s - (i + 1) * q
            if t < 0:
                break
            ans = (ans + C(p - 1, i) *
                   count_game(p - i - 1, t, q) *
                   gamesize *
                   inverse(i + 1)) % base
    return ans

if __name__ == "__main__":
    # 示例: 使用 n = 10 生成一组测试数据并输出结果
    # print(main(10))
    pass