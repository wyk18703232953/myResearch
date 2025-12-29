import random

def solve(i, j, k, R, G, B, dp):
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    best = 0
    if i > 0 and j > 0:
        best = max(best, R[i] * G[j] + solve(i - 1, j - 1, k, R, G, B, dp))
    if j > 0 and k > 0:
        best = max(best, G[j] * B[k] + solve(i, j - 1, k - 1, R, G, B, dp))
    if k > 0 and i > 0:
        best = max(best, B[k] * R[i] + solve(i - 1, j, k - 1, R, G, B, dp))
    dp[i][j][k] = best
    return best

def main(n):
    # 根据规模 n 生成测试数据：
    # 将 n 分成三部分，作为 nr, ng, nb
    nr = n // 3
    ng = (n - nr) // 2
    nb = n - nr - ng

    # 生成 R, G, B 的值（1~1000 的随机整数）
    R = [0] + sorted(random.randint(1, 1000) for _ in range(nr))
    G = [0] + sorted(random.randint(1, 1000) for _ in range(ng))
    B = [0] + sorted(random.randint(1, 1000) for _ in range(nb))

    dp = [[[-1] * (nb + 1) for _ in range(ng + 1)] for _ in range(nr + 1)]
    ans = solve(nr, ng, nb, R, G, B, dp)
    print(ans)

# 示例调用：可以按需修改 n
if __name__ == "__main__":
    main(9)