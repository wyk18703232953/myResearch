def main(n):
    # 将 n 映射为行数与列数，使规模随 n 线性增长
    # 行数和列数都与 n 挂钩，保证输入规模可控且可放大
    rows = max(1, n)
    cols = max(1, n)

    # 构造确定性的 01 字符串列表，长度为 rows，每个字符串长度为 cols
    # 使用简单算术关系 (i+j) % 2 来生成固定模式
    tc = [0] * cols
    ps = []
    for _ in range(rows):
        psa = [0] * cols
        for j in range(cols):
            if (j + _) % 2 == 0:
                psa[j] = 1
                tc[j] += 1
        ps.append(psa)

    ans = 'NO'
    for i in ps:
        c = 0
        for j in range(cols):
            if tc[j] - i[j] > 0:
                c += 1
        if c == cols:
            ans = 'YES'
            break

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 来改变规模
    main(10)