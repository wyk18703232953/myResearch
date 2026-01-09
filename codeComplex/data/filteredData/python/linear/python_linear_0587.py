def main(n):
    # 生成测试数据
    # 构造长度为 n 的二进制字符串 l 和查询次数 q 及其区间
    # 这里示例：l 为周期 "01" 重复，q = n，查询为 [1,1], [1,2], ..., [1,n]
    mod = 10**9 + 7
    l = ''.join('01'[(i % 2)] for i in range(n))  # 示例二进制串
    q = n
    queries = [(1, i) for i in range(1, n + 1)]

    # 前缀计数
    cnt1, cnt0 = [0] * (n + 1), [0] * (n + 1)
    for i in range(len(l)):
        if l[i] == '1':
            cnt1[i + 1] = cnt1[i] + 1
            cnt0[i + 1] = cnt0[i]

        else:
            cnt0[i + 1] = cnt0[i] + 1
            cnt1[i + 1] = cnt1[i]

    # 预计算 2 的幂
    max_len = n  # ones 最大不会超过 n
    pow2 = [1] * (max_len + 2)
    for i in range(1, max_len + 2):
        pow2[i] = (2 * pow2[i - 1]) % mod

    # 处理查询并输出
    for lq, rq in queries:
        ones = cnt1[rq] - cnt1[lq - 1]
        zeroes = cnt0[rq] - cnt0[lq - 1]
        t1 = (pow2[ones] - 1) % mod
        t2 = (t1 * (pow2[zeroes] - 1)) % mod
        # print((t1 + t2) % mod)
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)