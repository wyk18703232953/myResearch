def main(n):
    # 根据规模 n 生成测试数据，这里构造 k = n // 2 作为示例
    k = n // 2

    # 原始逻辑
    for i in range(100 * k + 100 * n):
        if i * (i + 1) == (n + k - i) * 2:
            # print(n - i)
            pass
            break


# 简单示例：当直接运行该文件时执行 main
if __name__ == "__main__":
    # 可以根据需要修改这里的 n，用于本地测试
    main(10)