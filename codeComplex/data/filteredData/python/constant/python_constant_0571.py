import random

def main(n: int):
    # 生成规模为 n 的测试数据：
    # 这里简单约定：
    #   N = n
    #   M, K, L 在 [1, n] 范围内随机生成（M 保证 <= N 且 > 0）
    if n <= 0:
        return

    N = n
    M = random.randint(1, max(1, N))  # 保证 1 <= M <= N
    K = random.randint(0, N)
    L = random.randint(0, N)

    # 原逻辑
    each = (K + L) // M
    if (K + L) % M != 0:
        each += 1

    if each * M > N:
        print(-1)
    else:
        print(each)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)