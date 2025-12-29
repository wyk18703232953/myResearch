import random

def main(n: int):
    # 生成测试数据
    # n: 总人数
    # m: 出租车数量，随机不超过 n
    m = random.randint(1, n)
    # 随机生成 n 个位置（1..10^9），并排序模拟一条线上的位置分布
    dist = sorted(random.randint(1, 10**9) for _ in range(n))
    # 随机选择 m 个位置作为有出租车的位置
    taxi = [0] * n
    taxi_indices = random.sample(range(n), m)
    for idx in taxi_indices:
        taxi[idx] = 1

    # 原逻辑开始
    dists = {}
    d = []
    for person in range(len(taxi)):
        if taxi[person]:
            dists[dist[person]] = 0
            d.append(dist[person])
    start = 0
    d.append(10**11)
    for person in range(len(taxi)):
        if taxi[person] == 0:
            while dist[person] > d[start + 1]:
                start += 1
            if abs(dist[person] - d[start]) <= abs(dist[person] - d[start + 1]):
                dists[d[start]] += 1
            else:
                dists[d[start + 1]] += 1
    # 输出结果（与原程序行为等价：顺序为字典遍历顺序）
    for key in dists:
        print(dists[key] if key != 10**11 else '', end=' ')
    print()


if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)