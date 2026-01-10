def getdict_from_list(n_list):
    d = {}
    for i in n_list:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def cdiv(n, k):
    return n // k + (n % k != 0)

def core_logic(n, d_list):
    d_list_sorted = sorted(d_list)
    return min(d_list_sorted[-2] - 1, n - 2)

def main(n):
    # 定义测试组数 t，与 n 线性相关，至少为 1
    t = max(1, n)

    results = []
    for case_idx in range(1, t + 1):
        # 为每组数据定义 n_case，保证规模随 n 增长
        # 这里令每组的 n_case = n + case_idx，至少为 3（避免越界）
        n_case = max(3, n + case_idx)

        # 构造长度为 n_case 的确定性数组 d_list
        # 示例构造：d[i] = (i * 2 + case_idx) % (n_case + 5) + 1
        d_list = [((i * 2 + case_idx) % (n_case + 5)) + 1 for i in range(n_case)]

        # 保持原程序核心逻辑不变
        ans = core_logic(n_case, d_list)
        results.append(ans)

    # 为了保持输出行为，打印所有结果
    for res in results:
        print(res)

if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)