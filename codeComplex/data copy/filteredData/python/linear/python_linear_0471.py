def main(n):
    # 根据 n 构造确定性数据
    # c: 长度为 n 的正整数数组
    # a: 长度为 n 的 0..n-1 的排列形式的“下一节点”数组，保证存在若干环
    if n <= 0:
        # print(0)
        pass
        return

    # 构造 c[i] = (i * 17 + 5) % 1000000007 + 1，保证正且确定
    MOD = 1000000007
    c = [(i * 17 + 5) % MOD + 1 for i in range(n)]

    # 构造一个简单有环结构的 a：
    # 前 n//2 个元素组成一个大环，其余每个元素自成一个 1 长度环
    a = [0] * n
    if n == 1:
        a[0] = 0

    else:
        half = n // 2
        if half == 0:
            half = 1
        # 0..half-1 构成环
        for i in range(half - 1):
            a[i] = i + 1
        a[half - 1] = 0
        # 其余位置形成自环
        for i in range(half, n):
            a[i] = i

    vis = [-1] * n
    ans = 0
    for i in range(n):
        ind = i
        while vis[ind] == -1:
            vis[ind] = i
            ind = a[ind]
        if vis[ind] == i:
            start = ind
            ind = a[ind]
            cost = c[start]
            while ind != start:
                if c[ind] < cost:
                    cost = c[ind]
                ind = a[ind]
            ans += cost
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)