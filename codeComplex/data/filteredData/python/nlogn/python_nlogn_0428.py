import random

def main(n: int):
    # 生成测试数据：n个整数，范围自定
    # 这里生成在 [-10**9, 10**9] 范围内的随机数
    l = [random.randint(-10**9, 10**9) for _ in range(n)]

    # 预计算不超过 10^18 的 2 的幂
    p = []
    i = 0
    while 2 ** i <= 10 ** 18:
        p.append(2 ** i)
        i += 1

    # 统计每个数的出现次数
    d = {}
    s = set()
    for x in l:
        s.add(x)
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    # 找出满足条件的元素集合 z
    z = set()
    for x in s:
        f = 1
        for val in p:
            e = val - x
            if e in s:
                if e == x and d[e] == 1:
                    continue
                f = 0
                break
        if f:
            z.add(x)

    # 计算答案
    ans = 0
    for x in z:
        ans += d[x]

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模自定义
    main(10)