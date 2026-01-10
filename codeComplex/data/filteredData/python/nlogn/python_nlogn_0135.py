def main(n):
    # 映射：n -> 输入规模
    # n 至少为 1
    if n <= 0:
        return

    # 构造确定性参数
    # m > k 保证进入主逻辑
    m = 2 * n + 5
    k = n // 2 + 1

    # 构造长度为 n 的数组 a
    # a[i] = (i % 7) + 1，且保证有足够大的值以可能到达 m
    a = [(i % 7) + 1 for i in range(1, n + 1)]

    # 为了保证在一些 n 下能到达 m，再在前面放一个与 n 有关的较大值
    # 如果 n 较大则这一项也较大，但仍是确定性的
    if n > 1:
        a[0] = n // 2 + 3

    # 保持原程序逻辑
    a.sort()
    a = a[::-1]

    if m <= k:
        print(0)
    else:
        c = 0
        while c < n:
            k = k + a[c] - 1
            c += 1
            if k >= m:
                print(c)
                return
        else:
            print(-1)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 进行规模实验
    main(10)