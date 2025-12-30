import random

def main(n: int):
    """
    n 作为规模参数，用于控制生成测试数据的范围。
    这里约定：
    - yellow, blue 在 [0, n] 范围内随机生成
    - y, g, b 在 [0, n] 范围内随机生成
    如需固定数据，可在此处修改为确定性生成方式。
    """
    # 生成测试数据
    yellow = random.randint(0, n)
    blue = random.randint(0, n)
    y = random.randint(0, n)
    g = random.randint(0, n)
    b = random.randint(0, n)

    count = 0

    yt = y * 2 + g
    bt = g + b * 3

    yc = yellow - yt
    if yc < 0:
        count += abs(yc)

    bc = blue - bt
    if bc < 0:
        count += abs(bc)

    print(count)


if __name__ == "__main__":
    # 示例：选择一个规模 n 运行
    main(10)