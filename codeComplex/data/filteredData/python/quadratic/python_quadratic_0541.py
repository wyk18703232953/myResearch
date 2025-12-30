import random

def main(n: int):
    # 生成测试数据：一个长度为 n 的数组 a[1..n]，满足 sum(a) 为偶数且 >= 2(n-1)
    # 原程序的 a[0] 没用，这里保持同样结构，a[1..n] 有意义
    if n <= 0:
        return

    # 简单生成：先给每个点 1~3 度，再微调以满足 sum 条件
    a = [0]
    degs = [random.randint(1, 3) for _ in range(n)]
    s = sum(degs)
    need = 2 * (n - 1)

    # 若总度太小，往上加
    while s < need:
        i = random.randrange(n)
        degs[i] += 1
        s += 1

    # 若总度与 2(n-1) 奇偶性不同，调一调
    if s % 2 != need % 2:
        i = random.randrange(n)
        degs[i] += 1
        s += 1

    # 现在 s >= need 且同奇偶，但原算法不保证可行性，这里只是生成“类似”的随机数据
    a.extend(degs)

    # 以下为原逻辑（去掉 input，直接使用 a 和 n）
    edge = []
    last, total_sum, ans = 0, 0, 0

    for i in range(1, n + 1):
        total_sum += a[i]

    for i in range(1, n + 1):
        if a[i] == 1:
            last = i
    if last != 0:
        a[last] = 0

    for i in range(1, n + 1):
        if a[i] > 1:
            if last:
                edge.append([last, i])
                ans += 1
            last = i

    for i in range(1, n + 1):
        if a[i] == 1 and last:
            edge.append([last, i])
            last = 0
            a[i] = 0
            ans += 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[j] == 1 and a[i] > 2:
                edge.append([i, j])
                a[i] -= 1
                a[j] -= 1

    if len(edge) != n - 1:
        print("NO")
    else:
        print("YES", ans)
        print(len(edge))
        for u, v in edge:
            print(u, v)


if __name__ == "__main__":
    # 示例：n=5 时运行一次
    main(5)