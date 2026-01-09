mod = 10**9 + 7

def fp(x, y):
    if y == 1:
        return x % mod
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
    numberOfPro = fp(2, k) % mod
    last = (n * numberOfPro) % mod
    first = ((n - 1) * numberOfPro + 1) % mod

    sumOfLast = last * (last + 1) % mod * inv(2) % mod
    sumOfFirst = first * (first - 1) % mod * inv(2) % mod

    num = 2 * (sumOfLast - sumOfFirst) % mod * inv(numberOfPro) % mod
    return num % mod

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里假设 k 的规模与 n 同阶，例如 k = n
    k = n
    ans = solve(n, k)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为测试规模
    main(10)