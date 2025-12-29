import random

def main(n: int):
    # 生成测试数据：a 为长度为 n 的整数数组
    # 这里示例生成 1 到 2n 范围内的随机整数
    a = [random.randint(1, 2 * n) for _ in range(n)]

    b = [0] * n
    for i in range(n):
        if i + 1 > a[i]:
            b[i] = i + 1
        else:
            q = (a[i] - (i + 1) + n) // n
            b[i] = i + 1 + q * n

    print(b.index(min(b)) + 1)


if __name__ == "__main__":
    # 示例运行：可修改 n 测试不同规模
    main(10)