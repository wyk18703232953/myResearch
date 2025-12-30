mod = 1000000000 + 7


def fp(x, y):
    if y == 1:
        return x
    if y == 0:
        return 1
    t = fp(x, y // 2) % mod
    if y % 2 == 1:
        return (t * t * x) % mod
    else:
        return (t * t) % mod


def inv(x):
    return fp(x % mod, mod - 2) % mod


def solve(n, k):
    if not n:
        return 0
    if not k:
        return (2 * n) % mod
    numberOfPro = fp(2, k)
    last = n * numberOfPro
    first = (n - 1) * numberOfPro + 1
    sumOfLast = (last) * (last + 1) * inv(2)
    sumOfFirst = first * (first - 1) * inv(2)
    num = 2 * (sumOfLast - sumOfFirst) * inv(numberOfPro)
    return num % mod


def main(n):
    # 根据规模 n 生成测试数据 (n, k)
    # 例如：k 取为 n 的一半（向下取整）
    k = n // 2
    ans = solve(n, k)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模自定义
    main(10)