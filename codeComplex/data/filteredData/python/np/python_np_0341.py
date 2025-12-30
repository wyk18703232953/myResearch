# by the authority of GOD     author: manhar singh sachdev #

import random

def main(n):
    mod = 10**9 + 7

    # 生成测试数据：
    # n 个人，每个人有（duration, genre）
    # genre ∈ {1,2,3}，原代码中存入前会减 1 变成 {0,1,2}
    # 同时生成目标时间 T，在这里设为所有 duration 之和的一半（向下取整）
    peo = []
    total_duration = 0
    for _ in range(n):
        duration = random.randint(1, 10)
        genre = random.randint(1, 3)
        peo.append([duration, genre])
        total_duration += duration

    T = total_duration // 2

    y = 1 << n
    dp = [[0] * 3 for _ in range(y)]
    # already taken ; genre

    # 调整 genre 到 {0,1,2}，并初始化单人子集的 dp
    for ind, person in enumerate(peo):
        person[1] -= 1
        dp[1 << ind][person[1]] = 1

    # 状态转移：集合 i，最后类型 j
    for i in range(y):
        for j in range(3):
            if not dp[i][j]:
                continue
            mask = 1
            for k in range(n):
                # 不能重复选，且类型不能等于 j
                if i & mask or peo[k][1] == j:
                    mask <<= 1
                    continue
                dp[i | mask][peo[k][1]] = (dp[i | mask][peo[k][1]] + dp[i][j]) % mod
                mask <<= 1

    # 枚举子集，计算总持续时间为 T 的方案数
    ans = 0
    for i in range(y):
        ans1, mask = 0, 1
        for j in range(n):
            if i & mask:
                ans1 += peo[j][0]
            mask <<= 1
        if ans1 == T:
            ans = (ans + sum(dp[i])) % mod

    # 返回结果和测试数据，方便调用者检查
    return ans, peo, T

if __name__ == '__main__':
    # 示例：n = 4
    ans, peo, T = main(4)
    print("people (duration, genre 1~3):")
    for d, g0 in peo:
        print(d, g0 + 1)
    print("Target T:", T)
    print("Answer:", ans)