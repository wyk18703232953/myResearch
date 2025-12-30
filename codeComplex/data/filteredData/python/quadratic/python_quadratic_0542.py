import random

def main(n: int):
    # 生成测试数据：构造一个长度为 n 的数组 a
    # 这里给出一种策略：随机生成，保证 sum(a) >= 2*n - 2 的概率较大
    if n <= 0:
        return

    # 基于 n 构造 a，既包含 1，又有较大值
    a = []
    base = max(1, (2 * n - 2) // max(1, n))  # 大致平均值
    for _ in range(n):
        # 随机取 [1, base+2] 范围内的值
        a.append(random.randint(1, max(2, base + 2)))

    # 原逻辑开始
    if sum(a) < (2 * n) - 2:
        print("NO")
        return
    else:
        one = []
        rst = []
        for i in range(0, n):
            if a[i] > 1:
                rst.append(i)
            else:
                one.append(i)

        ans = []

        # 先把 >1 的点链成一条链
        for i in range(1, len(rst)):
            ans.append((rst[i], rst[i - 1]))
            a[rst[i]] -= 1
            a[rst[i - 1]] -= 1

        # 将多余的 1 连接到有剩余度数的 rst 节点上
        for i in range(1, len(one)):
            for j in range(0, len(rst)):
                if a[rst[j]] > 0:
                    a[rst[j]] -= 1
                    ans.append((rst[j], one[i]))
                    break

        # 把第一个 1 连接到某个剩余度数的 rst 节点
        if len(one):
            for i in range(len(rst) - 1, -1, -1):
                if a[rst[i]] > 0:
                    ans.append((rst[i], one[0]))
                    break

        siz = min(len(one) + len(rst), 2 + len(rst)) - 1
        print("YES", siz)
        print(len(ans))
        for u, v in ans:
            print(u + 1, v + 1)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)