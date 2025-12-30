import random

def main(n: int) -> None:
    # 生成测试数据：
    # N 规模与 n 挂钩，其余参数在合法范围内随机生成
    N = n
    if N <= 0:
        print(-1)
        return

    # 为保证一定概率可行，M 在 [1, N] 内
    M = random.randint(1, N)

    # 随机生成 K, L，保证 K + L <= N 的概率较大
    # 先生成一个上界 S <= N
    S = random.randint(0, N)
    K = random.randint(0, S)
    L = S - K

    # 下面是原逻辑
    if N < M or K + L > N:
        print(-1)
    else:
        ans = (L + K - 1) // M + 1
        if ans * M <= N:
            print(ans)
        else:
            print(-1)


if __name__ == "__main__":
    # 示例：用不同规模调用 main
    main(10)