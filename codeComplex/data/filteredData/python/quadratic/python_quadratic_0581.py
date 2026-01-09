def main(n):
    # 将 n 解释为字符串长度，同时设置固定的 k 和测试用例数量 t
    # 为了可规模化，令:
    #   t = 3                      # 测试用例个数
    #   每个用例的 n_i = n         # 字符串长度
    #   每个用例的 k_i = n // 2 + 1（至少为 1，且不超过 n）
    t = 3
    results = []
    for case_id in range(t):
        cur_n = n
        k = max(1, min(cur_n, cur_n // 2 + 1))

        # 构造确定性的字符串 s，长度为 cur_n
        # 使用周期性 "RGB" 模式的偏移来生成：偏移依赖 case_id，保持确定性
        base = "RGB"
        offset = case_id % 3
        s_chars = [base[(i + offset) % 3] for i in range(cur_n)]
        s = "".join(s_chars)

        p = (k + 2) // 2
        l = "RGB" * p
        res = cur_n
        for i in range(cur_n - k + 1):
            c = 0
            for j in range(0, k):
                c += (s[i + j] != l[j])
            res = min(res, c)

            c = 0
            for j in range(1, k + 1):
                c += (s[i + j - 1] != l[j])
            res = min(res, c)

            c = 0
            for j in range(2, k + 2):
                c += (s[i + j - 2] != l[j])
            res = min(res, c)

        results.append(res)

    # 输出所有测试用例的结果，保持与原程序行为相似（逐行输出）
    for val in results:
        # print(val)
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模做时间复杂度实验
    main(1000)