import collections
import bisect
import random

def main(n: int):
    # 1. 生成规模为 n 的随机测试数据
    # 生成 n 段区间 [x, y]，保证 x <= y
    starting = []
    ending = []
    for _ in range(n):
        x = random.randint(0, 10**6)
        y = random.randint(0, 10**6)
        if x > y:
            x, y = y, x
        starting.append(x)
        ending.append(y)

    # 2. 原始逻辑
    ans = 0
    start_count = collections.Counter(starting)
    end_count = collections.Counter(ending)

    s = sorted(starting)
    e = sorted(ending)

    maxim = max(starting)
    minim = min(ending)

    for i in range(n):
        if starting[i] == maxim:
            if start_count[maxim] > 1:
                loc_max = maxim
            else:
                pos = bisect.bisect_left(s, maxim)
                loc_max = s[pos - 1]
        else:
            loc_max = maxim

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
    # 示例：调用 main，规模可自行调整
    main(10)