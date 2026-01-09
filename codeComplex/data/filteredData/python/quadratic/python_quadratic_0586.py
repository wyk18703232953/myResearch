def mismatch(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt

def run_single_case(n, k, s):
    from math import ceil
    check = ''
    for _ in range(ceil((k + 2) / 3)):
        check += 'RGB'
    ls = [check[i:i + k] for i in range(3)]
    m = n
    for i in range(n - k + 1):
        sub = s[i:i + k]
        for j in ls:
            m = min(m, mismatch(sub, j))
    return m

def main(n):
    # 解释规模映射：
    # T = n                      测试用例数量
    # 第 t 个用例：
    #   nt = n + t               字符串长度（随 t 线性增长）
    #   kt = max(1, nt // 2)     模式长度，保证 1 <= k <= n
    # 字符串 s 的确定性构造：周期 "RGB" 重复并再加上简单变化
    T = n
    results = []
    for t in range(1, T + 1):
        nt = n + t
        kt = max(1, nt // 2)
        base = "RGB"
        s_chars = []
        for i in range(nt):
            # 周期 + 轻微确定性扰动（不会引入随机性）
            idx = (i + t) % 3
            s_chars.append(base[idx])
        s = ''.join(s_chars)
        res = run_single_case(nt, kt, s)
        results.append(res)
    # 为避免大量输出，仅输出最后一个结果以及简单聚合信息
    if results:
        # print(results[-1])
        pass
if __name__ == "__main__":
    # 示例规模调用，可按需修改 n
    main(10)