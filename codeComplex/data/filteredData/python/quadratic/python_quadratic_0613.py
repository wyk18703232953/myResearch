import random

def main(n):
    # 生成测试数据：n, m, k 和数组 a
    # 这里示例：a 中元素在 1..10，m 在 1..n，k 在 0..10
    if n <= 0:
        return 0

    m = random.randint(1, n)
    k = random.randint(0, 10)
    a = [random.randint(1, 10) for _ in range(n)]

    sa = [0] * n
    ans = 0

    for i in range(n):
        sa[i] = a[i] - k
        s = a[i]
        for j in range(i - 1, max(-1, i - m - 1), -1):
            sa[i] = max(sa[i], sa[j] + s - k)
            s += a[j]
        if i < m:
            sa[i] = max(sa[i], s - k)
        sa[i] = max(sa[i], 0)
        ans = max(ans, sa[i])

    print(ans)
    return ans