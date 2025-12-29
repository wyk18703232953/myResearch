import random

def main(n: int):
    """
    n: 测试规模，用来控制生成的整数大小（例如最大为 10**n - 1）
    """
    if n <= 0:
        # 若n不合法，默认使用一个固定数
        x = 1
    else:
        # 根据n生成一个随机整数，范围 [0, 10**n - 1]
        upper = 10**n - 1
        x = random.randint(0, upper)

    # 原始逻辑：print(int(input()) // 2 + 1)
    result = x // 2 + 1

    # 输出测试数据和结果，便于调试
    print(x)
    print(result)


if __name__ == "__main__":
    # 示例：使用 n = 3 作为测试规模
    main(3)