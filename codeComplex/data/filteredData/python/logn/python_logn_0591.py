from math import sqrt

mod = 10 ** 9 + 7
mod2 = 998244353

S1 = 'abcdefghijklmnopqrstuvwxyz'
S2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def isprime(x):
    if x <= 1:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def main(n):
    # 生成测试数据：根据 n 构造 (a, b)
    # 简单方案：a = n*(n+1)//2 + n, b = n
    # 这样循环会有合理的规模
    a = n * (n + 1) // 2 + n
    b = n

    c = 0
    x = 0
    while not (c >= b and c - b + x == a):
        x += 1
        c += x
    print(a - x)


if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)