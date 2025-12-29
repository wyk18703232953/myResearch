import random

def main(n):
    # 生成测试数据：
    # k 为数组长度，设为 n 的 2~4 倍之间随机
    k = random.randint(2 * n, 4 * n)
    # 生成元素值，范围 1..n（可根据需要调整）
    a = [random.randint(1, n) for _ in range(k)]

    # 原逻辑开始
    d = {}
    for chr_ in a:
        if chr_ not in d:
            d[chr_] = 1
        else:
            d[chr_] += 1

    p = list(d.values())
    z = k // n
    if z == 0:
        print(0)
    else:
        o = []
        if len(a) >= n:
            o.append(1)
        for i in range(2, z + 1):
            c = 0
            for j in range(len(p)):
                c += p[j] // i
            if c >= n:
                o.append(i)
        print(max(o) if o else 0)


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)