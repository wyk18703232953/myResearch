import heapq
import random


def main(n: int):
    MOD_NUM = 10 ** 9 + 7

    # 生成测试数据：
    # 随机生成 x, y
    x = random.randint(1, 10 ** 9)
    y = random.randint(1, 10 ** 9)

    # 生成 n 个区间 [l, r]，保证 l < r
    # 时间范围可按规模线性扩展
    max_time = max(2 * n, 10)
    intervals = []
    for _ in range(n):
        l = random.randint(1, max_time - 1)
        r = random.randint(l + 1, max_time)
        intervals.append((l, r))

    # -------- 以下为原逻辑，仅去掉 input() 并用生成的数据 --------
    events = dict()
    for l, r in intervals:
        if l not in events:
            events[l] = []
        events[l].append(r)

    tv = []
    pq = []
    cost = 0

    for t in sorted(events):
        while tv and tv[0] < t:
            heapq.heappush(pq, -(x + heapq.heappop(tv) * y))

        for ri in sorted(events[t], reverse=True):
            if pq and -pq[0] > t * y:
                val = -heapq.heappop(pq)
                rj = (val - x) // y

                cost += (ri - rj) * y
                heapq.heappush(tv, ri)
            else:
                cost += x + (ri - t) * y
                heapq.heappush(tv, ri)
        cost %= MOD_NUM

    print(cost)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)