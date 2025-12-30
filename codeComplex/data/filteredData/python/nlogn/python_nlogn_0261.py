import random

def main(n):
    # 生成测试数据：n 个区间 [l, r]，1 <= l <= r <= 2n
    # 可以根据需要调整数据生成策略
    intervals = []
    for _ in range(n):
        l = random.randint(1, 2 * n)
        r = random.randint(l, 2 * n)
        intervals.append([l, r])

    def fn(s, e, qs, qe):
        # 判断区间 [s,e] 是否完全被 [qs,qe] 包含
        return qs <= s <= e <= qe

    ans = [-1, -1]
    # 加上原来的 index
    a = [[intervals[i][0], intervals[i][1], i] for i in range(n)]
    a.sort(key=lambda x: (x[0], x[1]))

    for i in range(n - 1):
        if fn(a[i][0], a[i][1], a[i + 1][0], a[i + 1][1]):
            ans = [a[i][2] + 1, a[i + 1][2] + 1]
            break
        elif fn(a[i + 1][0], a[i + 1][1], a[i][0], a[i][1]):
            ans = [a[i + 1][2] + 1, a[i][2] + 1]
            break

    print(*ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)