import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # n 表示幂指数的大小，同时用来控制 m 的范围
    # 这里生成 0 <= m < 2^(n+2) 的随机整数作为测试数据
    max_m = 1 << (n + 2)
    m = random.randrange(max_m)

    # 原逻辑：输出 m % 2^n
    result = m % (1 << n)
    print(result)


if __name__ == "__main__":
    # 示例：可在此修改 n 测试不同规模
    main(10)