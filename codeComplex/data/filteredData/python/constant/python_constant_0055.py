def main(n):
    # 生成规模为 n 的测试数据，这里简单设为 n 本身
    s = n

    t = len(str(s))
    L = ['4', '7']
    import copy
    for _ in range(t):
        L1 = copy.deepcopy(L)
        for m in L:
            L1.append(m + '4')
            L1.append(m + '7')
        L = L1
    L0 = list(map(int, L))
    cnt = 0
    for val in L0:
        if s % val == 0:
            cnt += 1
    if cnt > 0:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：以 100 为规模调用
    main(100)