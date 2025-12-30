import random

def main(n):
    # 生成测试数据
    # n : 最大元素值
    # 随机构造 m（元素个数）与 k（页大小）
    m = random.randint(1, n)
    k = random.randint(1, max(1, n // 10))

    # 生成一个严格递增的序列 l，长度为 m，元素在 [1, n] 内
    l = sorted(random.sample(range(1, n + 1), m))

    # 原逻辑
    out = 0
    d = 0

    while m > d:
        nex = l[d]
        page = (nex - d - 1) // k
        add = 1
        while d + add < m and (page * k) < l[d + add] - d <= (page + 1) * k:
            add += 1
        d += add
        out += 1

    print(out)

if __name__ == "__main__":
    # 示例：n 可以按需修改
    main(1000)