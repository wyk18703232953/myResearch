from copy import deepcopy
import random

def sol(n, m, k, aa, bb):
    if k & 1:
        return [[-1] * m for _ in range(n)]
    ans = [[float('inf')] * (m + 2) for _ in range(n + 2)]
    k >>= 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            ans[i][j] = min(aa[i][j], aa[i][j - 1], bb[i][j], bb[i - 1][j])
    for _ in range(k - 1):
        oans = deepcopy(ans)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                ans[i][j] = min(
                    aa[i][j] + oans[i][j + 1],
                    aa[i][j - 1] + oans[i][j - 1],
                    bb[i][j] + oans[i + 1][j],
                    bb[i - 1][j] + oans[i - 1][j]
                )

    ans = ans[1:-1]
    ans = [x[1:-1] for x in ans]
    ans = [[2 * x for x in a] for a in ans]
    return ans


def main(n):
    # 生成规模为 n 的测试数据：
    # 采用 m = n，k 为偶数以得到有意义结果
    m = n
    k = 2 * max(1, n // 2)

    # 随机权值范围
    MIN_W, MAX_W = 1, 10

    # 生成原始 aa, bb（未padding）
    aa_raw = [[random.randint(MIN_W, MAX_W) for _ in range(m)] for _ in range(n)]
    bb_raw = [[random.randint(MIN_W, MAX_W) for _ in range(m)] for _ in range(n - 1)] if n > 1 else []

    inf = float('inf')

    # 按原程序方式进行 padding
    aa = [[inf, *row, inf] for row in aa_raw]
    bb = [[inf, *row, inf] for row in bb_raw]

    pad_aa = [inf] * (m + 1)
    aa = [pad_aa, *aa, pad_aa]

    pad_bb = [inf] * (m + 2)
    bb = [pad_bb, *bb, pad_bb]

    ans = sol(n, m, k, aa, bb)
    print('\n'.join(' '.join(map(str, row)) for row in ans))


if __name__ == "__main__":
    # 示例：调用 main，规模可在此调整
    main(4)