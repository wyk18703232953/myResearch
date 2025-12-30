import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里约定：
    #   n 为除数（正整数）
    #   m 为 [1, n * 10] 范围内的随机正整数
    if n <= 0:
        raise ValueError("n must be a positive integer")
    m = random.randint(1, n * 10)

    # 原逻辑：输出 ceil(m / n)
    result = m // n + (1 if m % n else 0)
    print(result)

if __name__ == "__main__":
    # 示例：可在此处指定规模测试
    main(5)