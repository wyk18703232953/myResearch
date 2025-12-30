import random

def main(n: int):
    # 1) 生成测试数据
    # 生成一个长度为 n 的数组 d，元素为 1..n 的随机排列
    d = list(range(1, n + 1))
    random.shuffle(d)

    # 随机生成查询次数 m（1..n）
    m = random.randint(1, n)

    queries = []
    for _ in range(m):
        l = random.randint(1, n)
        r = random.randint(l, n)  # 确保 l <= r
        queries.append((l, r))

    # 2) 计算初始逆序对奇偶性
    odd = 0
    for i in range(n):
        for j in range(i, n):
            if d[i] > d[j]:
                odd ^= 1

    # 3) 处理查询并收集结果
    ans = []
    for l, r in queries:
        k = r - l + 1
        if (k * (k - 1) // 2) % 2:
            odd ^= 1
        ans.append("odd" if odd else "even")

    # 4) 输出（与原程序行为一致）
    print('\n'.join(ans))


if __name__ == "__main__":
    # 示例：可以修改 n 进行本地测试
    main(5)