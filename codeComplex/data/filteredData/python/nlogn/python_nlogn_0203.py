def check(mid, a, limit):
    res = []
    s = 0
    for r, t, id in a:
        if r >= mid and t + s <= limit:
            res.append(id + 1)
            s += t
        elif t + s > limit:
            break
        if len(res) == mid:
            break
    return res

def f(a, limit):
    a.sort(key=lambda s: s[1])
    ans = None
    lo = 0
    hi = len(a) + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        res = check(mid, a, limit)
        if len(res) >= mid:
            lo = mid + 1
            ans = (res, mid)
        else:
            hi = mid - 1
    print(ans[1])
    print(ans[1])
    print(*ans[0])

def main(n):
    # 映射含义：
    # n = 原程序中的 n（元素个数）
    # limit = 与 n 相关的确定性总时间限制
    limit = n * 5
    q = []
    # 生成确定性数据：
    # r = (i % (n + 1)) + 1  保证有足够多 r >= mid 的元素
    # t = (i % 7) + 1        任务时间为 1..7 的小整数
    for i in range(n):
        x = (i % (n + 1)) + 1
        y = (i % 7) + 1
        q.append((x, y, i))
    f(q, limit)

if __name__ == "__main__":
    main(10)