import random

def main(n: int):
    # 生成测试数据：t组测试，每组 (n, k)
    # 这里固定 t=5，可按需要修改
    t = 5
    test_cases = []

    for _ in range(t):
        # n 固定为参数 n
        nn = n

        # 粗略生成一个适配范围的 k
        # upper_bound 是一个比较松的上界，防止整数过大
        if nn >= 32:
            # 原逻辑：n >= 32 时不依赖 k 范围，任意正数即可
            k = random.randint(1, 10**6)
        else:
            # 构造一个上界估计值，用来随机 k
            # 和原代码中计算的 low/kk 的数量级一致即可
            md = [0]
            for j in range(1, nn):
                md.append(md[-1] * 4 + 1)

            low = 0
            co = -1
            kk = 0
            approx_max = 0
            for cut in range(1, nn + 1):
                low += (1 << cut) - 1
                co = 2 * co + 3
                kk += co * md[nn - cut]
                approx_max = max(approx_max, low + kk)

            # 避免上界太小
            upper = max(approx_max, 10)
            upper = min(upper, 10**9)
            k = random.randint(1, upper)

        test_cases.append((nn, k))

    # 按原逻辑处理并输出结果
    for nn, k in test_cases:
        if nn >= 32:
            print("YES %d" % (nn - 1))
        else:
            low = 0
            co = -1
            md = [0]
            for j in range(1, nn):
                md.append(md[-1] * 4 + 1)
            kk = 0
            found = 0
            for cut in range(1, nn + 1):
                low += (1 << cut) - 1
                co = 2 * co + 3
                kk += co * md[nn - cut]
                if k >= low and k <= low + kk:
                    print("YES %d" % (nn - cut))
                    found = 1
                    break
            if found == 0:
                print("NO")


# 示例调用（提交到评测时可删除或注释）
if __name__ == "__main__":
    main(10)