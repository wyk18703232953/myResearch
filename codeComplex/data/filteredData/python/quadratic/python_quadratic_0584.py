def main(n):
    # n 作为字符串长度规模；为了保证可测性：
    # - 测试用例数量 t = 3
    # - 第 i 个用例长度 = n + i
    # - k = max(1, (n + i) // 2)
    # - 字符串以周期 RGB 生成
    t = 3
    results = []

    for case_id in range(1, t + 1):
        curr_n = n + case_id  # 不同用例有不同的 n
        if curr_n <= 0:
            curr_n = 1
        k = curr_n // 2
        if k <= 0:
            k = 1
        if k > curr_n:
            k = curr_n

        # 构造字符串 s，长度为 curr_n，周期 "RGB"
        base_pattern = ['R', 'G', 'B']
        s_list = [base_pattern[i % 3] for i in range(curr_n)]
        s = "".join(s_list)

        ans = 10**9
        for i in range(curr_n - k + 1):
            x = s[i:i + k]
            curr = ['R', 'G', 'B']
            for l in range(3):
                m = 0
                z = l
                for ch in x:
                    if ch != curr[z]:
                        m += 1
                    z += 1
                    if z == 3:
                        z = 0
                if m < ans:
                    ans = m
        results.append(ans)

    for r in results:
        print(r)


if __name__ == "__main__":
    # 示例：使用 n = 10 运行一次
    main(10)