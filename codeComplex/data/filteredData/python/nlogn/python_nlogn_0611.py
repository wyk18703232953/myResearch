from bisect import bisect_left
import random

def main(n):
    # 参数：n 为区间数量规模
    # 随机生成测试数据：n 个区间 [l, r)，保证 l < r
    # 同时随机生成 c_tv, c_es
    random.seed(0)
    c_tv = random.randint(1, 10**6)
    c_es = random.randint(1, 10**6)

    start = []
    end = []
    add = 0

    # 生成 n 个区间，时间范围控制在 [0, 10^6]
    for _ in range(n):
        l = random.randint(0, 10**6 - 1)
        r = random.randint(l + 1, 10**6)
        add += (r - l)
        start.append(l)
        end.append(r)

    start.sort()
    end.sort()
    ans = add * c_es + n * c_tv
    M = 10**9 + 7
    v = [0] * (n + 1)

    for i in range(n):
        indx = bisect_left(end, start[i]) - 1
        k = indx
        while k >= 0 and (start[i] - end[k]) * c_es < c_tv and v[k] == 1:
            k -= 1
        if k == -1:
            continue
        if (start[i] - end[k]) * c_es < c_tv:
            ans -= c_tv - (start[i] - end[k]) * c_es
            v[k] = 1

    print(ans % M)


if __name__ == "__main__":
    # 示例：调用 main(10) 运行规模为 10 的测试
    main(10)