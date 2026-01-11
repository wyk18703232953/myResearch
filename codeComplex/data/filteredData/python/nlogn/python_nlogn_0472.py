def main(n):
    # 解释输入规模映射：
    # n: 原题中的数组长度 n
    # 这里我们令 k = max(1, n // 3)，保证 1 <= k <= n
    if n <= 0:
        return

    k = max(1, n // 3)
    if k > n:
        k = n

    # 确定性地构造数组 a，长度为 n
    # 使用简单的算术模式，保证可重复：
    # a[i] = (i * 7 + 3) % (2*n + 1)
    a = [(i * 7 + 3) % (2 * n + 1) for i in range(n)]

    # 原始核心逻辑
    p = sorted(a)
    p = p[-k:]
    s = sum(p)
    # print(s)
    pass
    idx = 0
    i = 0
    count = 0
    ans = []
    while len(ans) < k - 1:
        idx += 1
        count += 1
        if a[i] in p:
            p.remove(a[i])
            ans.append(count)
            count = 0
        i += 1
    for x in ans:
        # print(x, end=" ")
        pass
    # print(n - idx)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次可重复的实验
    main(10)