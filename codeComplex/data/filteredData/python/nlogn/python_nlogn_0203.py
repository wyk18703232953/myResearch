import random

def check(mid, a, limit):
    res = []
    s = 0
    for r, t, idx in a:
        if r >= mid and t + s <= limit:
            res.append(idx + 1)
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
    # 生成测试数据
    # 约定：n 为元素数量，limit 与 (r, t) 随机生成
    random.seed(0)
    limit = random.randint(max(1, n // 2), max(1, n * 2))
    q = []
    for i in range(n):
        # r 表示某种“需求值”，在 [0, n] 之间
        r = random.randint(0, n)
        # t 表示“耗时/代价”，在 [1, n] 之间
        t = random.randint(1, n)
        q.append((r, t, i))
    f(q, limit)

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)