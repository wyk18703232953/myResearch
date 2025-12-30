import random

def main(n: int):
    # 依据规模 n 生成测试数据
    # 将原本的 n 重命名为 N，避免与函数参数混淆
    N = n
    M = random.randint(1, max(1, 2 * N))  # 随机生成 m，范围可根据需要调整
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    # 原始逻辑
    if N > M:
        if N % M == 0:
            print(0)
        else:
            t1 = N % M
            print(min(t1 * b, (M - t1) * a))
    elif N == M:
        print(0)
    else:
        print(min(N * b, (M - N) * a))


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需要设置
    main(10)