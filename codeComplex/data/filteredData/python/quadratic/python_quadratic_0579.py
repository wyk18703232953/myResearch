def main(n):
    text = 'RGB' * 2222

    # 构造 T 组测试用例，令 T = n
    T = n

    results = []
    for t in range(T):
        # 构造每组的 n_t, k_t
        # 令字符串长度随 t 增长，最大不超过 3n+3，且至少为 1
        n_t = max(1, 3 * (t + 1))
        # k_t 在 [1, n_t] 内变化
        k_t = max(1, (t % n_t) + 1)

        # 构造长度为 n_t 的字符串 s_t，只由 'R', 'G', 'B' 组成
        # 使用简单确定性模式：周期为 3 的 RGB 序列偏移
        base = t % 3
        chars = ['R', 'G', 'B']
        s_t = ''.join(chars[(base + i) % 3] for i in range(n_t))

        # 以下是原算法逻辑
        ans = 2222
        for i in range(3):
            p = text[i: k_t + i]
            for j in range(n_t - k_t + 1):
                diff = 0
                for l in range(j, j + k_t):
                    if s_t[l] != p[l - j]:
                        diff += 1
                if diff < ans:
                    ans = diff
        results.append(ans)

    # 为了避免输出过大，仅输出最后一个结果
    if results:
        # print(results[-1])
        pass

    else:
        # print(0)
        pass
if __name__ == "__main__":
    main(10)