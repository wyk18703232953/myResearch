def main(n):
    # 确定性构造隐藏数组 a[1..n]
    # 需要满足存在 t = n//2，且存在 l 使得:
    # a[l] == a[(l + t - 1) % n + 1] 且 t 为偶数
    #
    # 这里构造一个周期为 t 的数组：
    # a[i] = i % t
    # 则对于任意 i，有 a[i] == a[i+t]（循环意义下）
    # 原程序通过交互式二分查找这个位置 l
    t = n // 2

    # 保持与原程序逻辑一致：若 t 为奇数，直接输出 -1
    if t & 1:
        # print('! -1')
        pass
        return

    # 构造数组（1-based 访问）
    a = [(i % t) for i in range(1, n + 1)]

    def ask(x):
        # 模拟交互：返回 a[x]
        # 保证与原程序的访问方式一致
        x = int(x)
        return a[x - 1]

    l = 1
    r = n
    while l < r:
        mid = (l + r) >> 1
        if ask(mid) >= ask((mid + t - 1) % n + 1):
            r = mid

        else:
            l = mid + 1
    # print('! %d' % l)
    pass
if __name__ == "__main__":
    # 示例：以 n=200 运行一次，用于时间复杂度实验
    main(200)