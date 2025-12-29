import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里生成 a, b 在 [1, n] 范围内的随机整数
    a = random.randint(1, max(1, n))
    b = random.randint(1, max(1, n))

    # 原始逻辑：输出 (b + a - 1) // a
    result = (b + a - 1) // a
    print(result)


if __name__ == "__main__":
    # 示例：以 n = 100 作为规模运行一次
    main(100)