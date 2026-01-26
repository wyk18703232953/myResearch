def main(n):
    # 确定性构造多组测试数据
    # 让测试组数 T 与 n 线性相关
    T = max(1, n // 5)
    results = []

    for t in range(1, T + 1):
        # 为每个测试构造 n_i, k_i
        # n_i 随测试编号线性增长，确保整体规模随 n 增大
        n_i = max(1, n + t)
        # k_i 在 1 到 n_i 之间，以确定性方式取值
        k_i = max(1, (t * 3) % n_i)
        if k_i > n_i:
            k_i = n_i

        # 构造字符串 s，长度为 n_i，由 'R','G','B' 三种字符组成
        # 使用简单算术保证确定性
        chars = ['R', 'G', 'B']
        s_list = [chars[(i * 2 + t) % 3] for i in range(n_i)]
        s = "".join(s_list)

        # 以下是原核心算法（从输入改为使用构造好的 n_i, k_i, s）
        p = (k_i + 2) // 2
        l = "RGB" * p
        res = n_i
        for i in range(n_i - k_i + 1):
            c = 0
            for j in range(0, k_i):
                c += (s[i + j] != l[j])
            res = min(res, c)

            c = 0
            for j in range(1, k_i + 1):
                c += (s[i + j - 1] != l[j])
            res = min(res, c)

            c = 0
            for j in range(2, k_i + 2):
                c += (s[i + j - 2] != l[j])
            res = min(res, c)

        results.append(res)

    # 输出所有测试结果
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 规模
    main(50)