import random

def main(n):
    # 生成测试数据
    # t：间隔阈值，取 0.0 ~ 10.0 区间的随机浮点数
    t = round(random.uniform(0.0, 10.0), 2)
    cont, ans = [], 2

    # 生成 n 个区间，每个区间由中心点和长度构成
    # 中心点：-50.0 ~ 50.0，长度：0.0 ~ 20.0
    for _ in range(n):
        hcenter = round(random.uniform(-50.0, 50.0), 2)
        hlen = round(random.uniform(0.0, 20.0), 2)
        cont.append([hcenter - hlen / 2, hcenter + hlen / 2])

    cont.sort(key=lambda it: it[0])

    for i in range(n - 1):
        gap = cont[i + 1][0] - cont[i][1]
        if gap > t:
            ans += 2
        elif gap == t:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例调用：n 为规模，可自行修改
    main(10)