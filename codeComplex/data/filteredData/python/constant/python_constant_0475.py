import random

def main(n: int):
    # 规模 n 决定 N 的大小范围，这里设定：
    # N 在 [1, n] 内随机生成
    # K 在 [0, 10 * n] 内随机生成
    if n <= 0:
        raise ValueError("n must be positive")

    N = random.randint(1, n)
    K = random.randint(0, 10 * n)

    # 原逻辑：输出 (K + N - 1) // N
    result = (K + N - 1) // N
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时按需调整 n
    main(10)