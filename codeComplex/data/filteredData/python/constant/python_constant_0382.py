import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # a, b, c, n 都在 [0, 2n] 范围内，保证规模与 n 相关
    a = random.randint(0, 2 * n)
    b = random.randint(0, 2 * n)
    c = random.randint(0, 2 * n)
    n_val = random.randint(0, 2 * n)

    # 原逻辑
    a -= c
    b -= c
    if a >= 0 and b >= 0:
        if (a + b + c) < n_val:
            n_val -= (a + b + c)
            print(n_val)
        else:
            print(-1)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)