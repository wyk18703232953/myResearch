def main(n):
    # n 作为测试用例数量
    results = []
    for t in range(1, n + 1):
        # 构造每个测试用例的规模 p_t，保证 p >= 1
        p = 2 + (t % 7)  # 在 2 到 8 之间循环
        # 构造数组 a，长度为 p，元素与 p 和 t 有确定性关系
        a = [(i * 2 + t) % (p + 3) + 1 for i in range(p)]
        a = sorted(a)
        if p == 2:
            results.append(0)
            continue
        k = a[-2] - 1
        results.append(min(k, p - 2))
    for r in results:
        print(r)


if __name__ == "__main__":
    main(10)