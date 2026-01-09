def solve(n, m, x, t):
    r = [0] * n
    d = [0] * m
    ans = [0] * m
    cr = 0
    cd = 0
    for i in range(n + m):
        if t[i]:
            d[cd] = x[i]
            cd += 1

        else:
            r[cr] = x[i]
            cr += 1
    cn = 0
    for i in range(m - 1):
        mid = (d[i] + d[i + 1]) // 2
        while cn < n and r[cn] <= mid:
            cn += 1
            ans[i] += 1
    ans[-1] += n - sum(ans)
    return ' '.join(str(i) for i in ans)


def main(n):
    # 定义规模含义：
    # 对于给定 n：
    #   m = max(1, n // 2)  # d 的个数
    #   n_r = max(1, n - m) # r 的个数
    #   总长度为 n_r + m
    if n <= 1:
        m = 1
        n_r = 1

    else:
        m = max(1, n // 2)
        n_r = max(1, n - m)

    total = n_r + m

    # 生成确定性的 x：严格递增，方便保持 r 和 d 各自有序
    # x[i] = 2 * i  保证数值间隔充足
    x = [2 * i for i in range(total)]

    # 生成确定性的 t，控制 r/d 的分布
    # 先构造一个长度为 total 的二进制序列，
    # 再根据需要调整，使得 0 的个数为 n_r，1 的个数为 m
    t = [0] * total
    # 先放 m 个 1 在偶数位置，如果不够再填奇数位置
    ones_needed = m
    for i in range(0, total, 2):
        if ones_needed > 0:
            t[i] = 1
            ones_needed -= 1

        else:
            break
    for i in range(1, total):
        if ones_needed <= 0:
            break
        if t[i] == 0:
            t[i] = 1
            ones_needed -= 1

    # 现在统计 1 的个数，确定 0 的个数是否为 n_r，不足则补 0，多余则裁剪前面的 0
    ones = sum(t)
    zeros = total - ones
    if zeros > n_r:
        # 需要把多余的 0 变成 1
        need_to_flip = zeros - n_r
        for i in range(total):
            if need_to_flip == 0:
                break
            if t[i] == 0:
                t[i] = 1
                need_to_flip -= 1
    elif zeros < n_r:
        # 需要把多余的 1 变成 0
        need_to_flip = n_r - zeros
        for i in range(total):
            if need_to_flip == 0:
                break
            if t[i] == 1:
                t[i] = 0
                need_to_flip -= 1

    # 再次统计，确保合法
    ones = sum(t)
    zeros = total - ones
    if ones != m:
        # 若仍有偏差，在末尾强制修正，保证确定性
        # 优先把末尾的元素改成 1 或 0
        # 调整 1 的个数
        if ones > m:
            # 多的 1 改为 0
            surplus = ones - m
            for i in range(total - 1, -1, -1):
                if surplus == 0:
                    break
                if t[i] == 1:
                    t[i] = 0
                    surplus -= 1
        elif ones < m:
            # 不足的 1 从后往前补
            lack = m - ones
            for i in range(total - 1, -1, -1):
                if lack == 0:
                    break
                if t[i] == 0:
                    t[i] = 1
                    lack -= 1

    # 最终截取前 total 个元素，保证长度不变
    t = t[:total]

    # 重新计算 r 和 d 的真实数量
    n_r_real = total - sum(t)
    m_real = sum(t)

    # 调用原算法
    result = solve(n_r_real, m_real, x, t)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)