from collections import defaultdict
import random

MOD = 10 ** 9 + 7

# 预计算组合数和 dp
MAXN = 1010
comb = [[1]]
for i in range(1, MAXN):
    x = [1]
    for j in range(1, i):
        x.append((comb[i - 1][j - 1] + comb[i - 1][j]) % MOD)
    x.append(1)
    comb.append(x)

dp = [1]
for i in range(1, MAXN):
    r = 0
    for k in range(i):
        r += dp[k] * comb[i - 1][k]
        r %= MOD
    dp.append(r)

def main(n: int):
    """
    n 为规模参数：
    - 令 m = n
    - 令列数 cols = n
    - 共生成 m 行，每行是长度为 cols 的 0/1 串，作为测试数据
    """
    m = n
    cols = n

    # 生成随机 0/1 矩阵数据：m 行，每行长度为 cols
    matrix = []
    for _ in range(m):
        row = [random.randint(0, 1) for _ in range(cols)]
        matrix.append(row)

    # 将原 input 读入逻辑替换为对 matrix 的处理
    ns = [0 for _ in range(m)]
    for j in range(cols):
        for i in range(m):
            ns[i] |= matrix[i][j] << j

    dd = defaultdict(int)
    for e in ns:
        dd[e] += 1

    ans = 1
    for b in dd.values():
        ans = ans * dp[b] % MOD

    print(ans)

if __name__ == '__main__':
    # 示例：以 n = 5 运行
    main(5)