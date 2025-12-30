import random

def popcount(i):
    assert 0 <= i < 0x100000000
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24

def main(n):
    # 生成测试数据
    N = n
    # 生成 TG: N 行，每行 [value, group]，group ∈ {1,2,3}
    TG = []
    for _ in range(N):
        value = random.randint(1, 10)
        group = random.randint(1, 3)
        TG.append([value, group])

    # 生成目标 T 为所有 value 的一半左右，增加可行解概率
    total_value = sum(x[0] for x in TG)
    T = total_value // 2

    mod = 10**9 + 7
    lim = 1 << N

    dp = [[0] * lim for _ in range(4)]
    for i in range(1, 4):
        dp[i][0] = 1

    for S in range(lim):
        if popcount(S) == 1:
            idx = (S & -S).bit_length() - 1
            g = TG[idx][1]
            dp[g][S] = 1
        for i in range(1, 4):
            val_i_S = dp[i][S]
            if val_i_S == 0:
                continue
            for j in range(N):
                if (S >> j) & 1:
                    continue
                g = TG[j][1]
                if i == g:
                    continue
                nxt = S | (1 << j)
                dp[g][nxt] = (dp[g][nxt] + val_i_S) % mod

    table = [0] * lim
    for S in range(lim):
        s_val = 0
        for j in range(N):
            if (S >> j) & 1:
                s_val += TG[j][0]
        table[S] = s_val

    ans = 0
    for S in range(lim):
        if table[S] == T:
            for i in range(1, 4):
                ans = (ans + dp[i][S]) % mod

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：n 可根据需要调整
    main(5)