def main(n):
    # 根据规模 n 生成测试数据：
    # 这里设定 k 为 n 的平方作为示例，可按需要调整生成规则
    k = n * n

    h = k // n
    if h * n < k:
        h += 1

    # print(h)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)，可按需要调整
    main(10)