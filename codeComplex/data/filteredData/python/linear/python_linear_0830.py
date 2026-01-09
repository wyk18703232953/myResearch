def solve(d, n, k):
    mv = sum(d[0:k])
    v = mv
    for i in range(1, n - k + 1):
        mv = mv + d[i + k - 1] - d[i - 1]
        v = min(v, mv)
    return v

def main(n):
    # 将 n 解释为字符串长度
    # 设定 k 为与 n 线性相关的窗口大小，保证 1 <= k <= n
    if n <= 0:
        return
    k = max(1, n // 3)

    # 构造确定性的多测试用例数量
    t = 3

    results = []
    for case_id in range(t):
        # 为每个用例构造确定性的 n_i, k_i, s_i
        # 这里 n_i 随 case_id 做微调，保持与 n 同阶
        n_i = max(1, n - case_id)
        k_i = min(k + case_id, n_i)

        # 构造确定性的字符串 s_i，使用简单周期和算术生成
        base = "RGB"
        s_list = []
        for i in range(n_i):
            # 通过 case_id 和 i 的线性关系改变字符分布
            idx = (i + case_id) % 3
            s_list.append(base[idx])
        s = "".join(s_list)

        st = base * (n_i // 3 + 3)
        diff1 = [0 for _ in range(n_i)]
        diff2 = [0 for _ in range(n_i)]
        diff3 = [0 for _ in range(n_i)]

        for i in range(n_i):
            if s[i] != st[i]:
                diff1[i] = 1
            if s[i] != st[i + 1]:
                diff2[i] = 1
            if s[i] != st[i + 2]:
                diff3[i] = 1

        ans = min(solve(diff1, n_i, k_i), solve(diff2, n_i, k_i), solve(diff3, n_i, k_i))
        results.append(ans)

    # 汇总输出，保证有可观察的输出规模
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)