def main(n):
    # 生成确定性输入数据：长度为 n 的整数数组 a
    # 使用简单的取模和加法构造，保证完全确定性
    a = [(i % n) + 1 for i in range(n)] if n > 0 else []
    # 原始算法逻辑开始
    n_local = len(a)
    u = n_local
    for i in range(n_local):
        j = i
        k = 0
        while j < n_local and a[j] > 0:
            k += 1
            t = j
            j = a[j] - 1
            a[t] = 0
        if k > 0:
            u += 1 - k % 2
    s = 'Petr'
    if u % 2 > 0:
        s = 'Um_nik'
    print(s)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 以进行规模实验
    main(10)