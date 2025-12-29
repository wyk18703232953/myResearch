import random

def main(n: int):
    # 根据规模 n 生成测试数据 (x, y)
    # 保证 1 <= x, y <= n
    x = random.randint(1, n)
    y = random.randint(1, n)

    if max(x - 1, y - 1) > max(n - x, n - y):
        print("Black")
    else:
        print("White")


if __name__ == "__main__":
    # 示例：可修改这里测试不同规模
    main(8)