import random

def main(n):
    # 1. 生成测试数据
    #   n: 区间数量
    #   随机生成 n 个 (x, w)，其中 x 和 w 在一定范围内
    xs = [random.randint(-10**6, 10**6) for _ in range(n)]
    ws = [random.randint(0, 10**6) for _ in range(n)]

    itvs = []
    for x, w in zip(xs, ws):
        itvs.append((x - w, x + w))

    # 2. 按右端点排序
    itvs.sort(key=lambda x: x[1])

    # 3. 区间调度：取最多个互不重叠区间
    ans = 0
    end = -(10**9 + 1)
    for l, r in itvs:
        if end <= l:
            ans += 1
            end = r

    print(ans)


if __name__ == "__main__":
    # 示例：可以根据需要修改规模 n
    main(10)