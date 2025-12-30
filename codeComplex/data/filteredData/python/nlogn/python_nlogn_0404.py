from random import randint

def main(n):
    # 生成规模为 n 的测试数据：n 个区间 [l, r]
    # 这里生成的区间在 [1, n] 范围内
    intervals = []
    for _ in range(n):
        l = randint(1, n)
        r = randint(1, n)
        if l > r:
            l, r = r, l
        intervals.append((l, r))

    # 原逻辑封装成函数，接收 intervals
    def solve(intervals):
        cnt = dict()
        for l, r in intervals:
            cnt[l] = cnt.get(l, 0) + 1
            cnt[r + 1] = cnt.get(r + 1, 0) - 1

        ans = [0] * (len(intervals) + 1)
        sk = sorted(cnt.keys())
        cnt_i = 0
        for ind, x in enumerate(sk[:-1]):
            cnt_i += cnt[x]
            ans[cnt_i] += sk[ind + 1] - x

        print(' '.join(str(v) for v in ans[1:]))

    solve(intervals)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)