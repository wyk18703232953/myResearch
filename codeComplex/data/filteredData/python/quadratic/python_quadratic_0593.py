import random

def main(n: int) -> int:
    # 生成测试数据
    # 这里构造一组可重复的伪随机数据，便于调试和测试
    random.seed(0)
    N = n
    M = max(1, n // 3)  # 保证 M >= 1，且相对小一些
    K = max(1, n // 5)  # 保证 K >= 1
    A = [random.randint(0, 10) for _ in range(N)]

    # 原逻辑开始
    S = [0]
    for a in A:
        S.append(S[-1] + M * a - K)

    MI = [10**50] * M
    ans = 0
    for i in range(N + 1):
        MI[i % M] = min(MI[i % M], S[i])
        for j in range(M):
            ans = max(ans, (S[i] - MI[(i - j) % M] - K * ((-j) % M)) // M)

    print(ans)
    return ans