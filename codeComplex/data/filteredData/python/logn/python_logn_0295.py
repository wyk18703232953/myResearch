MOD = 10 ** 9 + 7

def get(a, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return (get(a, n - 1) * a) % MOD
    else:
        b = get(a, n // 2) % MOD
        return (b * b) % MOD

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里令 x = n，k = n，用于构造一组随 n 变化的测试
    x = n
    k = n

    if x == 0:
        print(0)
    else:
        print((x * get(2, k + 1) - get(2, k) + 1) % MOD)


if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)