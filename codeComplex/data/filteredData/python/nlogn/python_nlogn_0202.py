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
    hi = 10**9
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
    # 根据 n 生成测试数据
    # 生成 limit：使得有一定概率能选出若干元素
    # 时间 t 在 [1, 100]，r 在 [0, n]，limit 约为 n * 50
    random.seed(0)
    limit = n * 50
    q = []
    for i in range(n):
        r = random.randint(0, n)
        t = random.randint(1, 100)
        q.append((r, t, i))
    f(q, limit)

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)