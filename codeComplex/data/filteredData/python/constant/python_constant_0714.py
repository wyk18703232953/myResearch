def main(n):
    # 生成测试数据：k 在 [1, n] 内，这里简单取 k = max(1, n // 2)
    if n <= 0:
        return
    k = max(1, min(n, n // 2))

    if n == k:
        # print('1' * n)
        pass
    elif k == 1:
        # print('0' + '1' * (n - 1))
        pass

    else:
        x = (n - k) // 2
        a = '0' * x + '1'
        # print(a * (n // (x + 1)) + '0' * (n % (x + 1)))
        pass
if __name__ == "__main__":
    # 示例：调用 main，给定一个规模 n
    main(10)