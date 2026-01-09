def main(n):
    # 根据规模 n 生成测试数据，这里假设：
    # n 为题目中的 n，k 取一个与 n 同规模的值，例如 k = n
    k = n

    # 原逻辑：输出 max(min(n, k-1) - k//2, 0)
    result = max(min(n, k - 1) - k // 2, 0)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)