def main(n):
    # 映射：n 作为测试用例数量 t
    t = n

    results = []
    for case_idx in range(t):
        # 为每个测试用例生成一个与 case_idx 相关的规模
        m = case_idx + 3  # 至少有 3 个元素，确保 lens[:-2] 有意义

        # 确定性生成长度数组 lens
        lens = [(i * (case_idx + 1)) % (m + 5) for i in range(1, m + 1)]
        lens.sort()

        # 原逻辑
        cnt = len([x for x in lens[:-2] if x > 0])
        results.append(min(cnt, lens[-2] - 1 if m >= 2 else 0))

    # 输出所有结果
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)