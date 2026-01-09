def main(n):
    # n 表示列表长度
    if n <= 0:
        return

    # 确定性生成测试数据：
    # 构造一个先严格递增后严格递减的序列（满足原判定条件）
    # 示例模式：0,1,2,...,peak,...,2,1,0
    # 为保证通用性，当 n < 3 时退化为简单递增序列
    if n < 3:
        l = [i for i in range(n)]

    else:
        peak = n // 2
        inc_part = list(range(peak + 1))              # 0..peak
        dec_part = list(range(peak - 1, -1, -1))      # peak-1..0
        l = (inc_part + dec_part)[:n]

    to = l.index(max(l))
    ok = 1
    for i in range(1, to):
        if l[i] <= l[i - 1]:
            ok = 0
            break
    for i in range(to + 1, n):
        if l[i] >= l[i - 1]:
            ok = 0
            break
    if ok:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)