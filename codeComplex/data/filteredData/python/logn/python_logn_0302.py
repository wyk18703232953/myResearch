def modularExponentiation(x, n, M):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return modularExponentiation((x * x) % M, n // 2, M)
    else:
        return (x % M * modularExponentiation((x * x) % M, (n - 1) // 2, M) % M) % M


def main(n):
    """
    n: 规模参数，用于生成测试数据
    这里用 n 生成 (n, k) 测试数据：
        示例：令 k = n
    可根据需要修改生成规则
    """
    c = 10**9 + 7
    k = n  # 根据规模 n 生成测试数据，这里简单设为 k = n

    a = (n % c * modularExponentiation(2, k + 1, c) % c) % c
    b = (modularExponentiation(2, k, c) % c - 1 % c + c) % c

    if n == 0:
        print("0")
    else:
        print((a % c - b % c + c) % c)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)