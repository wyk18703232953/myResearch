def main(n):
    """
    参数 n 作为规模，用于生成测试数据：
    - 生成 T = n 组测试
    - 对于每组：N = i (1..n)，K = 2^(i+2) - 1，保证不同规模
    结果直接打印，与原逻辑一致。
    """
    def solve_one(N, K):
        cur_usage = 0
        reslog = 0
        cnts = dict()

        # 第一阶段
        while True:
            reslog += 1
            cur_usage += (1 << reslog) - 1
            if reslog != N:
                cnts[reslog] = (((1 << reslog) - 2) << 1) + 1

            if cur_usage + (1 << (reslog + 1)) - 1 > K or reslog == N:
                break

        K -= cur_usage

        # 第二阶段
        while K > 0:
            if len(cnts) == 0:
                break
            # 原代码每轮只处理一个 key（任意一个），这里保持顺序稳定性：
            key = next(iter(cnts))
            K -= cnts[key]
            if key + 1 >= N:
                del cnts[key]
                continue
            if (key + 1) not in cnts:
                cnts[key + 1] = 0
            cnts[key + 1] += cnts[key] * 4
            del cnts[key]

        if K <= 0:
            print('YES %d' % (N - reslog))
        else:
            print('NO')

    # 生成测试数据并求解
    T = n
    for i in range(1, T + 1):
        N = i
        # 选一个随规模增长的 K（可根据需要调整）
        K = (1 << (i + 2)) - 1
        solve_one(N, K)


if __name__ == "__main__":
    # 示例：运行 n=5 规模
    main(5)