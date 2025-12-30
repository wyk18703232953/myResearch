import random

def main(n):
    # 随机生成测试数据 a, b, c, n_param
    # 保证 n_param 与规模 n 同数量级，避免溢出
    n_param = max(1, n)

    # 生成非负整数 a, b, c，范围可根据规模调整
    # 这里设置在 [0, 2*n_param] 之间
    a = random.randint(0, 2 * n_param)
    b = random.randint(0, 2 * n_param)
    c = random.randint(0, 2 * n_param)

    # 原逻辑
    if c > a or c > b:
        print(-1)
    else:
        val = n_param - ((a - c) + (b - c)) - c
        print(val if 0 < val <= n_param else -1)


if __name__ == "__main__":
    # 示例：按某个规模调用 main
    main(10)