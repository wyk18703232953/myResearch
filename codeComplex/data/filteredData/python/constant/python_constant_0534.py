import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里设定 m 在 [0, n * 10] 范围内，保持量级相关
    m = random.randint(0, n * 10)

    # 原逻辑：
    # ans = m // n + min(1, m % n)
    # 注意：需避免 n 为 0 导致除零错误
    if n == 0:
        raise ValueError("n must be non-zero for this computation.")

    ans = m // n + min(1, m % n)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)