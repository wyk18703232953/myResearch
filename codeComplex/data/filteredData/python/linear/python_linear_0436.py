def main(n):
    m = int(n ** 0.5)
    a = []

    # 根据 n 生成测试数据（此处逻辑与原程序一致，本身就是使用 n 生成序列 a）
    for i in range(0, n, m):
        for j in range(i, min(i + m, n)):
            a.append(min(i + m, n) - j + i)

    # print(' '.join(str(_) for _ in a))
    pass
if __name__ == "__main__":
    # 示例：调用 main，规模为 100
    main(100)