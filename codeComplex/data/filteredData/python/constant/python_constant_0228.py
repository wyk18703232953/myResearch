import random

def main(n: int):
    # n 用作生成数据的规模控制参数，这里简单设定：
    # a, b 在 [0, n] 范围内
    # x, y, z 在 [0, n] 范围内
    random.seed(0)  # 固定随机种子，保证结果可复现

    a = random.randint(0, n)
    b = random.randint(0, n)
    x = random.randint(0, n)
    y = random.randint(0, n)
    z = random.randint(0, n)

    ans = max(0, 2 * x + y - a) + max(0, 3 * z + y - b)
    print(ans)


if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(10)