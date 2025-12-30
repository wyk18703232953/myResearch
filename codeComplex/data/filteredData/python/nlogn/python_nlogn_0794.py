import random

def main(n):
    # 生成测试数据
    # 约定：k 在 [1, n] 之间随机生成，a 为严格递增数组
    if n <= 0:
        return

    k = random.randint(1, n)
    # 生成严格递增数组 a
    a = []
    cur = random.randint(0, 10)
    for _ in range(n):
        step = random.randint(1, 10)
        cur += step
        a.append(cur)

    # 原始逻辑开始
    s = []
    for q in range(n - 1):
        s.append([a[q + 1] - a[q], q])
    s.sort(reverse=True)
    d = {q[1] for q in s[:k - 1]}
    ans = 0
    q1 = a[0]
    for q in range(n - 1):
        if q in d:
            ans += a[q] - q1
            q1 = a[q + 1]
    ans += a[-1] - q1

    # 输出结果（以及可选测试数据，视需要可注释）
    print("n =", n)
    print("k =", k)
    print("a =", a)
    print("answer =", ans)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)