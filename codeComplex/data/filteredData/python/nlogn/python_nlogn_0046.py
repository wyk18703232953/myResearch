def main(n):
    # n 作为列表长度
    if n <= 0:
        return
    # 确定性生成测试数据：1 到 n 的递增序列
    p = [i for i in range(1, n + 1)]

    x = max(p)
    idx = p.index(x)
    if p[idx] == 1:
        p[idx] = 2

    else:
        p[idx] = 1
    p.sort()
    # print(' '.join(str(i) for i in p))
    pass
if __name__ == "__main__":
    main(10)