def f(q):
    from collections import defaultdict
    q.sort()
    d = defaultdict(int)
    for l, r in q:
        d[l] += 1
        d[r + 1] -= 1
    res = 0
    prev = None
    ans = [0] * (len(q) + 1)
    for i in sorted(d.keys()):
        if prev is None:
            prev = i

        else:
            ans[res] += i - prev
            prev = i
        res += d[i]
    return ans[1:]


def main(n):
    # 生成 n 个区间 (l, r)，满足 l <= r，且完全确定性
    # 例如：l = i, r = 2*i (i 从 1 到 n)
    q = [(i, 2 * i) for i in range(1, n + 1)]
    res = f(q)
    # 为了避免输出过大，仅在前若干项规模下打印全部结果
    # 实际做时间复杂度实验时，可以注释掉打印，仅保留算法运行
    # print(*res)
    pass
if __name__ == "__main__":
    # 示例调用，可按需要修改 n 的取值进行实验
    main(10)