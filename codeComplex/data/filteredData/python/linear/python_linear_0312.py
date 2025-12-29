import random

def main(n):
    # 1. 生成测试数据
    # 约定：m 在 [1, n] 范围内随机，a[i] 在 [0, 10**9] 范围内随机
    if n <= 0:
        return

    m = random.randint(1, n)
    a = [random.randint(0, 10**9) for _ in range(n)]

    # 2. 原始逻辑
    t = n // m
    remain = [[] for _ in range(m)]
    for i in range(n):
        x = a[i] % m
        remain[x].append(i)

    ans = 0
    f = []
    for i in range(2 * m):
        cur = i % m
        while len(remain[cur]) > t:
            elm = remain[cur].pop()
            f.append([elm, i])
        while len(remain[cur]) < t and len(f) != 0:
            elm, j = f.pop()
            remain[cur].append(elm)
            delta = abs(i - j)
            a[elm] += delta
            ans += delta

    # 3. 输出结果
    print(ans)
    print(*a)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)