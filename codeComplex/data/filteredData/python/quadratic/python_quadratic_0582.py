def solve(n, k, s):
    sf = 'RGB' * (k + 2)

    max_s = 0
    for i in range(n - k + 1):
        for j in range(3):
            count = 0
            for b in range(k):
                if sf[j + b] == s[i + b]:
                    count += 1
            if count > max_s:
                max_s = count

    return k - max_s


def main(n):
    # n 作为总字符规模，构造若干组测试用例
    # 设每组长度为 base_len，组数为 t
    if n <= 0:
        return

    base_len = 10
    if n < base_len:
        base_len = n
    t = max(1, n // base_len)

    results = []
    for q in range(t):
        # 为每个用例构造 n_i, k_i, s_i
        # 这里让每个用例的长度随 q 线性变化，总体规模与 n 同阶
        ni = max(1, base_len + q % (base_len))
        ki = max(1, ni // 2)

        # 构造确定性的字符串 s_i
        # 使用循环 'RGB' 与位置索引的简单规则
        pattern = "RGB"
        s_list = [pattern[(i + q) % 3] for i in range(ni)]
        s = "".join(s_list)

        res = solve(ni, ki, s)
        results.append(res)

    # 为防止 Python 优化掉计算，汇总输出一个确定性结果
    total = 0
    for x in results:
        total ^= x
    # print(total)
    pass
if __name__ == "__main__":
    main(10000)