import random

def main(n):
    # 生成 n 组测试数据 (a, b, c)，保证非负，且 c 有一定概率小于 a 或 b
    test_cases = []
    for _ in range(n):
        # 控制范围，避免数值过大
        c = random.randint(0, 100)
        # 让 a、b 有时大于 c，有时小于等于 c
        if random.random() < 0.5:
            a = random.randint(0, 100)
        else:
            a = random.randint(0, c if c > 0 else 0)
        if random.random() < 0.5:
            b = random.randint(0, 100)
        else:
            b = random.randint(0, c if c > 0 else 0)
        test_cases.append((a, b, c))

    # 按原逻辑处理并输出
    for a, b, c in test_cases:
        if (a > c or b > c):
            print(-1)
        else:
            if (a % 2 + b % 2 == 1):
                print(c - 1)
            elif (a % 2 == b % 2 == c % 2):
                print(c)
            else:
                print(c - 2)


if __name__ == "__main__":
    # 示例：生成并处理规模为 10 的测试
    main(10)