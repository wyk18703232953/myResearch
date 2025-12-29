from collections import defaultdict
import random

def f(q):
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
    # 生成 n 个随机区间，区间端点范围可按需调整
    q = []
    for _ in range(n):
        l = random.randint(0, 10 * n)
        r = random.randint(0, 10 * n)
        if l > r:
            l, r = r, l
        q.append((l, r))

    result = f(q)
    print(*result)

if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)