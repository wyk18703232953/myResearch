def main(n: int):
    # 生成测试数据：原代码中 input() 表示一个非负整数
    # 这里用 n 作为该整数
    x = n

    # 保持原始逻辑：从 x 递减到 0，每次减 2，然后求和
    result = sum(i for i in range(x, -1, -2))

    # 输出结果
    # print(result)
    pass


# 示例调用（提交到评测系统时通常不需要）
if __name__ == "__main__":
    # 可以修改这里的 n 进行本地测试
    main(10)