import random

def main(n):
    # 生成测试数据
    # n 作为规模，这里示例：N = n，M 和 K 也由 n 推导或固定
    N = n
    if N <= 0:
        print(0)
        return

    # 可根据需要调整下面两行的规则
    M = max(1, min(N, 5))      # 示例：M 取 1 到 5 之间且不超过 N
    K = max(1, N // 3)         # 示例：K 与 N 成比例

    # 生成数组 A 的测试数据，这里使用随机整数
    random.seed(0)             # 固定种子便于复现
    A = [random.randint(-10, 10) for _ in range(N)]

    # 原始逻辑
    bv = 0
    for ms in range(M):
        cv = 0
        for i in range(ms, N):
            v = A[i]
            if i % M == ms:
                v -= K
                cv = max(0, cv)
            cv += v
            bv = max(bv, cv)
    print(bv)


if __name__ == "__main__":
    # 示例调用
    main(10)