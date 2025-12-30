import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 令 m 在 [0, 2^(n+2)) 区间内随机取值，用于测试取模效果
    m = random.randint(0, 1 << (n + 2))

    # 原逻辑：输出 m % (1 << n)
    result = m % (1 << n)
    print(result)

if __name__ == "__main__":
    # 示例：可手动修改 n 测试不同规模
    main(5)