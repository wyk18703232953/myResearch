M = 1000000007

def a(k):
    if k > 0:
        l = a(k // 2)
        return (l * l * (k % 2 + 1)) % M
    else:
        return 1

def main(n):
    """
    n: 规模参数，用于生成测试数据。
       这里生成测试数据为 [n, 2*n]。
    """
    # 根据规模 n 生成原程序所需的两个整数
    data = [n, 2 * n]  # data[0] 对应原来的 n[0]，data[1] 对应原来的 n[1]

    if data[0] == 0:
        print(0)
    else:
        l = a(data[1])
        print((2 * (data[0] % M) * l - l + 1) % M)

if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模运行
    main(10)