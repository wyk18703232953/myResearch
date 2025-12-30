import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据（此处 n 仅用于控制数据范围）
    #    根据原逻辑，A, B, x, y, z 为整数，这里用 n 控制它们的上界
    upper = max(1, n)  # 防止 n 为 0 或负数
    A = random.randint(0, upper)
    B = random.randint(0, upper)
    x = random.randint(0, upper)
    y = random.randint(0, upper)
    z = random.randint(0, upper)

    # 2. 原始逻辑
    nA = 2 * x + y
    nB = 3 * z + y
    r = 0
    if nA > A:
        r += nA - A
    if nB > B:
        r += nB - B

    # 3. 输出结果
    print(r)


if __name__ == "__main__":
    # 示例：调用 main(10) 生成规模为 10 的一组测试数据并计算
    main(10)