def main(n):
    # n 作为测试用例数量 T
    T = n
    results = []
    for t in range(T):
        # 为每个测试用例构造一个确定性的数组 a
        # 令当前用例的规模随 t 变化：长度为 t+3，元素为 (i + t) % 10 + 1
        size = t + 3
        a = [(i + t) % 10 + 1 for i in range(size)]
        a.sort()
        res = min(len(a) - 2, max(a[-2] - 1, 0))
        results.append(res)
    for r in results:
        print(r)


if __name__ == "__main__":
    main(5)