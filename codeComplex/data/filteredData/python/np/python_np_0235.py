import random

def suma_o_resta(a, b):
    return (a & (1 << b))

def diferencia(s1, d):
    if s1:
        s1.sort()
        if s1[-1] - s1[0] >= d:
            return s1
        else:
            # remove the largest and recurse
            s1.pop()
            return diferencia(s1, d)
    return s1

def no_sets(v, n, l, r, d):
    s = []
    cont = 0
    for x in range(1 << n):
        for i in range(n):
            if suma_o_resta(x, i) > 0:
                s.append(v[i])
        s = diferencia(s, d)
        if s:
            ssum = sum(s)
            if l <= ssum <= r:
                cont += 1
        s = []
    return cont

def main(n):
    # 生成测试数据：
    # v 为 n 个不同正整数，范围适度即可
    # l, r 为区间，x 为差值下界
    random.seed(0)

    v = sorted(random.sample(range(1, max(3 * n, 10) + 1), n))
    # 确保有一定概率存在满足条件的集合
    total_sum = sum(v)
    l = total_sum // 4 if total_sum // 4 > 0 else 1
    r = total_sum
    x = max(1, (max(v) - min(v)) // 3)

    result = no_sets(v, n, l, r, x)
    print(result)

if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)