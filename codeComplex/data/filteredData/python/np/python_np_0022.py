#!/usr/bin/env python3
import random

def main(n):
    # 生成测试数据
    # n: 议员数量
    # k: 贿赂总额度（以10为单位的次数），这里示例设为 n * 5
    # A: 常数参数，这里示例设为 100
    k = n * 5
    A = 100

    global senators, bribe, mx_bribe

    # 生成每个议员的 (lvl, loy)
    # lvl: 1 ~ 1000
    # loy: 0 ~ 100
    senators = []
    mx_bribe = 0
    for _ in range(n):
        lvl = random.randint(1, 1000)
        loy = random.randint(0, 100)
        senators.append((lvl, loy))
        mx_bribe += (100 - loy) // 10

    bribe = [0] * n

    def calc(votes):
        bsum, cnt, p = 0, 0, 1.0
        for i, s in enumerate(senators):
            if votes & (1 << i):
                p *= (s[1] + bribe[i]) / 100
                cnt += 1
            else:
                p *= (100 - s[1] - bribe[i]) / 100
                bsum += s[0]

        if cnt > (n / 2):
            return p
        else:
            return p * A / (A + bsum)

    def dfs(cur, rk):
        if cur >= n:
            if rk > 0:
                return 0.0
            sm = 0.0
            for i in range(1 << n):
                sm += calc(i)
            return sm

        mx = 0.0
        for i in range(rk + 1):
            if i * 10 + senators[cur][1] > 100:
                break
            bribe[cur] = i * 10
            tmp = dfs(cur + 1, rk - i)
            if tmp > mx:
                mx = tmp
        return mx

    result = dfs(0, min(k, mx_bribe))
    print(result)


if __name__ == "__main__":
    # 示例调用：n = 5
    main(5)