import random

def main(n: int):
    # 根据 n 生成测试数据，这里简单示例为：使用给定的 n 本身作为规模
    # 如果需要可在此增加复杂测试数据生成逻辑
    if n < 3:
        print(n)
        return
    if n % 2 == 1:
        print(n * (n - 1) * (n - 2))
    else:
        if n % 3 == 0:
            g = n - 2
        else:
            g = n
        print((n - 1) * (n - 3) * g)


if __name__ == "__main__":
    # 示例：生成一个用于测试的 n（这里使用固定或随机值都可以）
    # 可根据需要修改测试用 n 的生成策略
    test_n = 10  # 示例固定值
    # test_n = random.randint(1, 100)  # 或者使用随机测试
    main(test_n)