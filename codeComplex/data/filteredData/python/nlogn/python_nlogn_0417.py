from collections import Counter
import random

def main(n):
    # 1. 生成测试数据：n 个区间 [l, r]，确保 l <= r
    intervals = []
    MAX_COORD = max(1, n * 2)
    for _ in range(n):
        l = random.randint(1, MAX_COORD)
        r = random.randint(1, MAX_COORD)
        if l > r:
            l, r = r, l
        intervals.append((l, r))

    # 2. 原逻辑开始
    count_left = Counter()
    count_right = Counter()

    for l, r in intervals:
        count_left[l] += 1
        count_right[r] += 1

    count = [0] * (n + 1)

    pts = sorted(set(count_left.keys()) | set(count_right.keys()))
    if not pts:
        print(' '.join(map(str, count[1:])))
        return

    c = 0
    prev = pts[0]

    for pt in pts:
        if count_left[pt]:
            count[c] += pt - prev - 1
            c += count_left[pt]
            count[c] += 1
            c -= count_right[pt]
        else:
            count[c] += pt - prev
            c -= count_right[pt]
        prev = pt

    print(' '.join(map(str, count[1:])))


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)