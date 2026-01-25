import math
import collections
import bisect

def main(n):
    if n <= 0:
        print(0)
        return

    # 构造确定性的区间数据：长度为 n 的起点/终点数组
    # 起点递增，终点递增并且都 >= 对应起点，保证逻辑可执行
    starting = [i for i in range(n)]
    ending = [i + (i % 3) + 1 for i in range(n)]

    ans = 0
    start_count = collections.Counter(starting)
    end_count = collections.Counter(ending)
    s = starting.copy()
    s.sort()
    e = ending.copy()
    e.sort()
    maxim = max(starting)
    minim = min(ending)

    for i in range(n):
        if starting[i] == maxim:
            if start_count[maxim] > 1:
                loc_max = maxim
            else:
                pos = bisect.bisect_left(s, maxim)
                loc_max = s[pos - 1] if pos - 1 >= 0 else maxim
        else:
            loc_max = maxim

        if ending[i] == minim:
            if end_count[minim] > 1:
                loc_min = minim
            else:
                pos = bisect.bisect_right(e, minim)
                if pos < len(e):
                    loc_min = e[pos]
                else:
                    loc_min = minim
        else:
            loc_min = minim

        ans = max(ans, loc_min - loc_max)

    print(ans)


if __name__ == "__main__":
    # 示例调用，可按需要调整 n 进行规模化实验
    main(10)