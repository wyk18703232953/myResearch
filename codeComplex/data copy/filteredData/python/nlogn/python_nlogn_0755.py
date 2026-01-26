def main(n):
    # n 表示测试用例数量 T
    T = n
    results = []

    for t in range(T):
        # 为第 t 个测试用例生成数组规模 m
        m = max(2, (t + 2) * 3)

        # 生成确定性数组 a，长度为 m，元素递增
        a = [(i * 2 + t) % (3 * m + 5) for i in range(m)]
        a.sort()

        res = min(len(a) - 2, a[-2] - 1)
        results.append(res)

    # 为了保证一些输出，返回结果列表
    return results


if __name__ == "__main__":
    # 示例：以 n=5 作为规模运行
    out = main(5)
    for v in out:
        # print(v)
        pass