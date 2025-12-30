import random

def main(n: int):
    # 生成规模为 n 的测试数据：
    # 这里假设 n 作为数值上界，用于控制输入数据的大小。
    # 可以根据需要调整生成策略。
    a = random.randint(0, n)
    b = random.randint(0, n)
    x = random.randint(0, n)
    y = random.randint(0, n)
    z = random.randint(0, n)

    r = 0

    yellow = 2 * x
    blue = 3 * z
    green = y

    if a > yellow:
        a -= yellow
    else:
        r += abs(a - yellow)
        a = 0

    if b > blue:
        b -= blue
    else:
        r += abs(b - blue)
        b = 0

    if a > green:
        a -= green
    else:
        r += abs(a - green)

    if b > green:
        b -= green
    else:
        r += abs(b - green)

    print(r)


if __name__ == "__main__":
    # 示例：使用 n = 100 作为规模
    main(100)