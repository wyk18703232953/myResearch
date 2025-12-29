def main(n):
    # 1. 根据规模 n 生成测试数据
    # 原程序固定使用 14 个坑位，这里保持逻辑不变，仅根据 n 控制数据范围
    # 例如：每个 a[i] 在 [0, n] 之间
    import random
    random.seed(0)
    a = [random.randint(0, n) for _ in range(14)]

    mr = 0
    for t in range(14):
        b = list(a)
        m = b[t]
        k = t
        i = 1
        b[k] = 0
        while m > 0:
            if m // 14 == 0:
                b[(k + i) % 14] += 1
                m -= 1
                i += 1
            else:
                q = m // 14
                for c in range(14):
                    b[c] += q
                m -= 14 * q
        p = sum(x for x in b if x % 2 == 0)
        mr = max(p, mr)

    print(mr)


if __name__ == "__main__":
    # 示例：使用 n = 100 作为规模
    main(100)