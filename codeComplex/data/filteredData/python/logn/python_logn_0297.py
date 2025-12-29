# -*- coding: utf-8 -*-

MOD = 10 ** 9 + 7

def modulus(a, b, m):
    if b == 0:
        return 1
    if b == 1:
        return a % m

    result = int(modulus(a, b // 2, m))

    if b % 2 == 0:
        return int(((result % m) * (result % m)) % m)
    else:
        return int(((result % m) * (result % m) * (a % m)) % m)

def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

def main(n):
    """
    根据规模 n 生成一组测试数据 (x, k)，并执行原逻辑。
    这里示例：令 x = n，k = n。
    如需其他生成策略，可按需求修改。
    """
    x = n
    k = n

    if x == 0:
        print(0)
    elif k != 0:
        ans = (modulus(2, k + 1, MOD) * (x % MOD)) % MOD
        ans = (ans - modulus(2, k, MOD) % MOD + 1 + MOD) % MOD
        print(int(ans))
    else:
        print(int((x % MOD) * 2 % MOD))

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)