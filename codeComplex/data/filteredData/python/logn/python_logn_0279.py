import sys
import random

def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y >>= 1
        x = (x * x) % p
    return res

MOD = 10**9 + 7

def main(n):
    # 根据规模 n 生成测试数据：
    # 让 r, k 与 n 同量级，且为非负整数
    r = random.randint(0, n)
    k = random.randint(0, n)

    if r == 0:
        print(0)
        return

    ans = (((power(2, k + 1, MOD) * (r % MOD)) % MOD) - power(2, k, MOD) + 1) % MOD
    print(ans)

if __name__ == "__main__":
    # 这里给一个默认规模，也可以在外部调用 main(n)
    main(10**6)