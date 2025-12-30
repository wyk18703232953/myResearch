import random

def main(n: int):
    """
    n 作为规模参数，这里用来控制随机数的上限：
    - yellow, blue, x, y, z 都在 [0, n] 区间内生成
    """
    # 1. 根据 n 生成测试数据
    yellow = random.randint(0, n)
    blue = random.randint(0, n)
    x = random.randint(0, n)
    y = random.randint(0, n)
    z = random.randint(0, n)

    # 2. 原逻辑
    answer1 = x * 2 + y - yellow
    answer2 = z * 3 + y - blue
    if answer1 > 0:
        if answer2 > 0:
            print(answer1 + answer2)
        else:
            print(answer1)
    else:
        if answer2 > 0:
            print(answer2)
        else:
            print(0)

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)