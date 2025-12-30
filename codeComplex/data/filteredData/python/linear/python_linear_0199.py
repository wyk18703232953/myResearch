import random

def main(n):
    # 生成测试数据
    # A, B, C, T 的取值范围可以根据需要调整
    A = random.randint(1, 10)
    B = random.randint(1, 10)
    C = random.randint(1, 10)
    T = random.randint(1, 100)

    # 生成 n 个 t_i，保证 0 <= t_i <= T
    t = [random.randint(0, T) for _ in range(n)]

    # 原逻辑
    if B > C:
        result = n * A
    else:
        t.sort()
        c = 0
        for i in t:
            c += (T - i) * (C - B) + A
        result = c

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(5)，规模为 5
    main(5)