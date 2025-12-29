def modularExponentiation(x, n, M):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return modularExponentiation((x * x) % M, n // 2, M)
    else:
        return (x % M * modularExponentiation((x * x) % M, (n - 1) // 2, M) % M) % M


def main(n):
    """
    n: 规模参数，这里用作原代码中的 n
    根据 n 生成测试数据：令 k = n（可按需调整生成规则）
    返回原程序最终的计算结果
    """
    c = 10**9 + 7
    k = n  # 生成测试数据：令 k 等于 n

    a = (n % c * modularExponentiation(2, k + 1, c) % c) % c
    b = (modularExponentiation(2, k, c) % c - 1 % c + c) % c

    if n == 0:
        return 0
    else:
        return (a % c - b % c + c) % c


if __name__ == "__main__":
    # 示例：调用 main(10)
    print(main(10))