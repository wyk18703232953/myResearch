def main(n):
    # 这里根据 n 自动生成一个 m，可按需要调整规则
    # 示例：令 m = n（生成 n x n 的网格）
    m = n

    r = []
    rappend = r.append
    for i in range(1, (n >> 1) + 1):
        for j in range(1, m + 1):
            rappend(str(i) + ' ' + str(j))
            rappend(str(n + 1 - i) + ' ' + str(m + 1 - j))
    if n & 1:
        for i in range(1, (m >> 1) + 1):
            rappend(str((n + 1) >> 1) + ' ' + str(i))
            rappend(str((n + 1) >> 1) + ' ' + str(m + 1 - i))
        if m & 1:
            rappend(str((n + 1) >> 1) + ' ' + str((m + 1) >> 1))
    # print('\n'.join(r))
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值做测试
    main(5)