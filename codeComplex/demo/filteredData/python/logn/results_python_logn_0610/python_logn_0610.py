import math as ma


def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    gg = find_gcd(x, y)
    return (x * y // gg)


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main(n):
    # 根据规模 n 生成测试数据 (n, k)
    # 这里简单设定 k = n^2，保证 n+k 非负且随规模增长
    k = n * n

    d = ma.sqrt(9 + 8 * (n + k))
    gp = (-3 + d) / 2
    result = int(n - gp)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：使用规模 n = 10 运行
    main(10)