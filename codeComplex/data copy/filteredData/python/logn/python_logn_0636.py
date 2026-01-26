def main(n):
    """
    将原逻辑封装为 main(n)，其中：
    - 使用 n 作为 actions（动作次数/规模）
    - end_total_candies 由 n 生成测试数据，这里设为 end_total_candies = n * (n + 1) // 2 的一半，保证相对合理
    """
    actions = n
    # 根据 n 生成一个测试 end_total_candies，这里采用一个简单的函数：
    # 总和约为 1+2+...+n 的一半
    end_total_candies = (n * (n + 1) // 2) // 2

    candies = 1
    if actions == 1:
        # print(0)
        pass
        return

    for i in range(1, actions):
        candies = candies + i + 1
        if candies >= end_total_candies + (actions - i - 2):
            # print(candies - end_total_candies)
            pass
            return


if __name__ == "__main__":
    # 示例：以 n=10 运行
    main(10)