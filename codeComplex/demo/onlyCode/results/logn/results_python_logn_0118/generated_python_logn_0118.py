import random

p = 10 ** 9 + 7

# 预留的组合数工具（原代码未使用）
inv = [0] * 300001
fact = [0] * 300001


def ncr_util():
    inv[0] = inv[1] = 1
    fact[0] = fact[1] = 1
    for i in range(2, 300001):
        inv[i] = (inv[i % p] * (p - p // i)) % p
    for i in range(1, 300001):
        inv[i] = (inv[i - 1] * inv[i]) % p
        fact[i] = (fact[i - 1] * i) % p


def solve(l, r):
    ans, a, b = 0, 0, 0
    mul = 2 ** 60
    for _ in range(61):
        ch1, ch2 = 0, 0
        if a + mul <= l:
            a += mul
            ch1 = 1
        if b + mul <= l:
            b += mul
            ch2 = 1
        if ch1 ^ ch2 == 1:
            ans += mul
        elif ch1 == 0 and ch2 == 0:
            if a + mul <= r:
                a += mul
                ans += mul
            elif b + mul <= r:
                b += mul
                ans += mul
        mul //= 2
    return ans


def main(n):
    """
    n: 规模参数，用于控制测试数据范围。
       我们生成一组区间 [l, r]，0 <= l <= r <= 2^n - 1（n 至多 60）。
    """
    max_bit = min(n, 60)
    if max_bit <= 0:
        # 退化情况，固定一个小区间
        l, r = 0, 0
    else:
        upper = (1 << max_bit) - 1
        l = random.randint(0, upper)
        r = random.randint(l, upper)
    print(solve(l, r))


if __name__ == "__main__":
    # 示例调用：可按需修改 n
    main(20)