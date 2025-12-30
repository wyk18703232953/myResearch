import random

def main(n):
    # 生成 n 个随机区间的中心 x 和半径 w
    # 可根据需要调整生成范围
    xs = [random.randint(-10**6, 10**6) for _ in range(n)]
    ws = [random.randint(0, 10**6) for _ in range(n)]

    intervals = []
    for x, w in zip(xs, ws):
        left = x - w
        right = x + w
        intervals.append((left, right))

    intervals.sort(key=lambda x: x[1])

    left = -1000000007
    ans = 0
    for i in range(n):
        if intervals[i][0] >= left:
            ans += 1
            left = intervals[i][1]
    print(ans)


if __name__ == "__main__":
    # 示例：n=10，可根据需要修改或在外部调用 main(n)
    main(10)