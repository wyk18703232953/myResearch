import random

def main(n: int):
    # 生成测试数据：x, y 在 [1, n] 范围内
    x = random.randint(1, n)
    y = random.randint(1, n)

    # 原始逻辑
    if n - x + n - y >= x - 1 + y - 1:
        print("White")
    else:
        print("Black")


if __name__ == "__main__":
    # 示例：可自行修改 n 来测试不同规模
    main(8)