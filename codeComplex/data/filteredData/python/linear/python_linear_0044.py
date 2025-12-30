import random

def main(n):
    # 生成测试数据：n 和 k，数组 a
    # 这里设置 k 在 [1, min(n, 20)] 内，避免过大导致几乎无有效段
    if n <= 0:
        return

    k = random.randint(1, min(n, 20))
    # 为了提升出现不同元素的概率，取值范围稍大
    max_val = max(2 * k, 10)
    a = [random.randint(1, max_val) for _ in range(n)]

    # 原逻辑开始
    q = {0}
    e = 0
    l = []
    for i in range(n):
        if a[i] not in q:
            e += 1
            q.add(a[i])
        if e == k:
            e = 0
            q = {0}
            l.append(i)

    w = 10**5
    t = 0
    for i in l:
        e = 0
        q = {0}
        for j in range(i, -1, -1):
            if a[j] not in q:
                e += 1
                q.add(a[j])
            if e == k:
                if w > len(q):
                    w = j + 1
                    t = i + 1
                break

    if len(set(a)) >= k:
        print(w, t)
    else:
        print(-1, -1)


if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)