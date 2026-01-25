def main(n):
    # 确定性生成输入数据
    # A, B, C, T 为常量参数，可根据需要调整
    A = 2
    B = 3
    C = 5
    T = n + 10  # 让 T 随规模变化，始终大于大部分 t[i]

    # 生成长度为 n 的 t 列表，保证 0 <= t[i] <= T
    # 使用简单算术构造确保确定性
    t = [i % (T + 1) for i in range(n)]

    # 以下为原算法逻辑
    if B > C:
        print(n * A)
    else:
        c = 0
        t.sort()
        for i in t:
            c += (T - i) * (C - B) + A
        print(c)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)