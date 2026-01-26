def main(n):
    # 映射：输入规模 n -> 原程序中的 n, k
    # 为了保持确定性，这里令 k = n
    original_n = n
    k = n

    result = None
    limit = 100 * k + 100 * original_n
    for i in range(limit):
        if i * (i + 1) == (original_n + k - i) * 2:
            result = original_n - i
            break

    if result is not None:
        # print(result)
        pass
if __name__ == "__main__":
    # 示例调用：可以修改 n 观察规模变化
    main(10)