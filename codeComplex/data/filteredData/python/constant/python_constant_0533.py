import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里假设 n 为题目中的 n，m 随规模生成
    if n <= 0:
        raise ValueError("n must be positive")
    m = random.randint(1, n * 10)

    # 原逻辑：输出 ceil(m / n)
    if m % n != 0:
        result = m // n + 1
    else:
        result = m // n

    print(result)

if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(5)