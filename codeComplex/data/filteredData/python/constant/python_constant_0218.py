import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里假设 n 控制数值范围：[-n, n]
    a = random.randint(-n, n)
    b = random.randint(-n, n)
    x = random.randint(-n, n)
    y = random.randint(-n, n)
    z = random.randint(-n, n)

    p = a - ((x * 2) + y)
    q = b - ((z * 3) + y)

    if p < 0 and q < 0:
        print(abs(p) + abs(q))
    elif p < 0:
        print(abs(p))
    elif q < 0:
        print(abs(q))
    else:
        print(0)


if __name__ == "__main__":
    # 示例：将规模设置为 10
    main(10)