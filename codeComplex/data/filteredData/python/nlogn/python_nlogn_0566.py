import random

def main(n):
    # 生成测试数据：随机生成 n 个人的左右约束 l, r
    # 为了保证有解，这里通过随机 candies 构造合法的 l, r
    candies = list(range(1, n + 1))
    random.shuffle(candies)

    l = []
    r = []
    for i in range(n):
        # 计算左侧比当前糖果多的人数
        l_count = sum(1 for c in candies[:i] if c > candies[i])
        # 计算右侧比当前糖果多的人数
        r_count = sum(1 for c in candies[i + 1:] if c > candies[i])
        l.append(l_count)
        r.append(r_count)

    # 以下为原逻辑
    s = [(i, sum(v)) for i, (v) in enumerate(zip(l, r))]
    ss = sorted(s, key=lambda a: a[1])

    candies_calc = [0] * n
    for p in ss:
        candies_calc[p[0]] = n - p[1]

    ll = [0]
    for i in range(1, n):
        ll.append(sum(1 for c in candies_calc[:i] if c > candies_calc[i]))

    rr = [0]
    for i in range(n - 2, -1, -1):
        rr.append(sum(1 for c in candies_calc[i:] if c > candies_calc[i]))

    for i in range(n):
        if ll[i] != l[i]:
            print("NO")
            return
        if rr[n - 1 - i] != r[i]:
            print("NO")
            return
    print("YES")
    print(' '.join(map(str, candies_calc)))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)