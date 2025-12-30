def main(n):
    # 根据 n 生成测试数据
    # 这里构造一个示例：N = n, 随机感弱的确定性数据，便于调试
    # 你可以按需要修改这部分数据生成逻辑
    N = n
    M = max(1, n // 3)      # 保证 M >= 1
    K = max(1, n // 5)      # 保证 K >= 1
    A = [(i * 2 + 3) % 10 for i in range(N)]

    # 以下为原算法逻辑
    S = [0]
    for a in A:
        S.append(S[-1] + M * a - K)

    MI = [10 ** 50] * M
    ans = 0
    for i in range(N + 1):
        mi_idx = i % M
        if S[i] < MI[mi_idx]:
            MI[mi_idx] = S[i]
        for j in range(M):
            idx = (i - j) % M
            cand = (S[i] - MI[idx] - K * ((-j) % M)) // M
            if cand > ans:
                ans = cand

    print(ans)


if __name__ == "__main__":
    # 示例调用
    main(10)