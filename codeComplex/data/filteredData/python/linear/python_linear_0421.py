def main(n):
    # 映射规则：
    # n = 数组长度
    # x = n 的按位取反（在一个固定掩码下），保证可重复且确定
    if n <= 0:
        return

    # 设定一个固定掩码，使得 x 与数组元素之间有一定的按位关系
    MASK = (1 << 17) - 1  # 0..131071
    x = (~n) & MASK

    # 生成确定性数组：arr[i] = (i * (i + 1)) & MASK
    arr = [(i * (i + 1)) & MASK for i in range(n)]

    # 原程序中的上界 100100 足够覆盖 MASK 范围
    SIZE = 100100
    f = [0] * SIZE
    s = [0] * SIZE
    can = [False] * SIZE

    for i in range(n):
        val = arr[i]
        if val < SIZE:
            f[val] += 1
        ax = val & x
        if ax < SIZE:
            s[ax] += 1
            if ax != val:
                can[ax] = True

    ans = 3
    for i in range(SIZE):
        if f[i] >= 2:
            ans = 0
            break
        if f[i] == 1 and s[i] >= 1:
            if can[i]:
                if 1 < ans:
                    ans = 1
        if s[i] >= 2:
            if 2 < ans:
                ans = 2

    if ans == 3:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 以做规模实验
    main(10)