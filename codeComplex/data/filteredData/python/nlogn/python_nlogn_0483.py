import random

def main(n):
    # 生成测试数据：
    # k 为数组长度，取 [n, 3n] 范围内随机值
    k = random.randint(n, 3 * n)
    # 数组元素取值范围 [1, n]，保证有重复，利于频数统计
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
        print(max(o))


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改
    main(10)