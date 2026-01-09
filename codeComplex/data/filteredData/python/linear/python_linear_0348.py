def main(n):
    # 原程序结构：
    # 第一行：n, k
    # 接下来 k 行：l, r（但不使用）
    # 然后根据 n 输出 1010... 交替的字符串
    
    # 这里将输入规模 n 直接作为原程序中的 n
    # 构造确定性的 k 和区间 (l, r)
    k = n  # 令查询次数与 n 同规模
    
    # 生成 k 个确定性的区间 [l, r]，不影响最终输出，仅保持结构
    intervals = []
    for i in range(1, k + 1):
        l = (i % n) + 1 if n > 0 else 1
        r = n - (i % n)
        if r < l:
            l, r = r, l
        intervals.append((l, r))
    
    # 保持原算法逻辑：仅依据 n 输出交替的 1 和 0
    output = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            output.append('0')

        else:
            output.append('1')
    # print(''.join(output))
    pass
if __name__ == "__main__":
    main(10)