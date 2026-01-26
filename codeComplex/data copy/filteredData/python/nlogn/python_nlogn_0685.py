def main(n):
    # 映射 n 为问题规模：
    # m = n（g 的长度），b 的长度为 max(1, n//2)
    if n <= 0:
        return
    m = n
    len_b = max(1, n // 2)

    # 确定性生成 b 和 g
    # b 为非递减序列，g 为非递减序列，且保证 max(b) <= min(g) 一般成立或不成立都可用于实验
    b = [i for i in range(1, len_b + 1)]
    g = [i + len_b for i in range(1, m + 1)]

    # 原算法逻辑
    if max(b) > min(g):
        # print(-1)
        pass
        return

    b.sort()
    res = sum(g) + sum(b[:-1]) * m
    if b[-1] in g:
        # print(res)
        pass

    else:
        # print(res + b[-1] - b[-2])
        pass
if __name__ == "__main__":
    main(10)