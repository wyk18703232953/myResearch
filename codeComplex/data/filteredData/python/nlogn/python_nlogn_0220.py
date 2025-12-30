import random

def main(n: int):
    # 生成测试数据
    # N 为规模，取 N = n（至少为 1）
    N = max(1, n)

    # 生成一个非降序列 E（便于 E[j] - E[i] 的逻辑）
    # 先生成随机递增步长，再前缀和
    base = random.randint(0, 10)
    steps = [random.randint(0, 5) for _ in range(N)]
    E = [base]
    for s in steps:
        E.append(E[-1] + s)
    E = E[1:]  # 去掉第一个占位，保留长度 N

    # 生成 U，使得有一定几率 E[j] - E[i] <= U 有解
    # 取 U 在 [0, max(1, E[-1] - E[0])] 范围内
    if N >= 2:
        U = random.randint(0, max(1, E[-1] - E[0]))
    else:
        U = random.randint(0, 10)

    # 原逻辑
    maxu = -1
    j = 2
    if N < 3:
        print(-1)
        return

    for i in range(N - 2):
        j = max(i + 2, j)
        if E[j] - E[i] > U:
            continue
        while j < N and E[j] - E[i] <= U:
            j += 1
        j -= 1
        maxu = max(maxu, (E[j] - E[i + 1]) / (E[j] - E[i]))

    print(maxu)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)