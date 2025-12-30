import random
import collections
import bisect

def main(n):
    # 1. 生成规模为 n 的测试数据：n 个区间 [x, y]，保证 x <= y
    #    这里随机生成在 [0, 10^6] 范围内的整数
    starting = []
    ending = []
    for _ in range(n):
        x = random.randint(0, 10**6)
        y = random.randint(0, 10**6)
        if x > y:
            x, y = y, x
        starting.append(x)
        ending.append(y)

    # 2. 按原逻辑处理
    ans = 0
    start_count = collections.Counter(starting)
    end_count = collections.Counter(ending)

    s = sorted(starting)
    e = sorted(ending)

    maxim = max(starting)
    minim = min(ending)

    for i in range(n):
        # 处理最大起点
        if starting[i] == maxim:
            if start_count[maxim] > 1:
                loc_max = maxim
            else:
                pos = bisect.bisect_left(s, maxim)
                loc_max = s[pos - 1]
        else:
            loc_max = maxim

        # 处理最小终点
        if ending[i] == minim:
            if end_count[minim] > 1:
                loc_min = minim
            else:
                pos = bisect.bisect_right(e, minim)
                loc_min = e[pos]
        else:
            loc_min = minim

        ans = max(ans, loc_min - loc_max)

    print(ans)


if __name__ == "__main__":
    # 示例调用：n 可以按需修改
    main(10)