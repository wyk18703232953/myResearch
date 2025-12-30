import random

MOD = 10**9 + 7

def main(n: int) -> int:
    # 生成长度为 n 的随机字符串列表，每个元素是 "s" 或 "f"
    s = ['s' if random.randint(0, 1) == 0 else 'f' for _ in range(n)]

    dps = [[0] * (n + 3) for _ in range(n + 1)]
    dpf = [[0] * (n + 3) for _ in range(n + 1)]

    for k in range(n + 1):
        dps[0][k] = 1

    for pos, char in enumerate(s):
        if char == "s":
            for depth in range(pos + 2):
                dps[pos + 1][depth] = (
                    dpf[pos][depth]
                    - dpf[pos][depth - 1]
                    + dps[pos][pos]
                    - dps[pos][depth - 1]
                )
                dps[pos + 1][depth] += dps[pos + 1][depth - 1]
                dps[pos + 1][depth] %= MOD

            for p in range(pos + 2, n + 1):
                dpf[pos + 1][p] += dpf[pos + 1][p - 1]
                dpf[pos + 1][p] %= MOD
        else:
            for depth in range(1, pos + 2):
                dpf[pos + 1][depth] = (
                    dpf[pos][depth - 1]
                    - dpf[pos][depth - 2]
                    + dps[pos][pos]
                    - dps[pos][depth - 2]
                )
                dpf[pos + 1][depth] += dpf[pos + 1][depth - 1]
                dpf[pos + 1][depth] %= MOD

            for p in range(pos + 2, n + 1):
                dpf[pos + 1][p] += dpf[pos + 1][p - 1]
                dpf[pos + 1][p] %= MOD

    ans = dps[n][n] % MOD
    print(ans)
    return ans