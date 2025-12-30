import random

def main(n: int):
    # 生成规模为 n 的测试数据：a, b 在 [0, 2^n - 1] 范围内
    upper = (1 << n) - 1
    a = random.randint(0, upper)
    b = random.randint(0, upper)

    if a == b:
        print(0)
    else:
        x = a ^ b
        c = 0
        while x:
            x = x // 2
            c += 1
        print((1 << c) - 1)


if __name__ == "__main__":
    # 可在此处指定 n 测试，例如：
    main(5)