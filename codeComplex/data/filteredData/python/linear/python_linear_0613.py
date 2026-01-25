def main(n):
    # 输入结构识别与规模映射：
    # 原程序输入：
    # 1) 单个整数 n
    # 2) 长度为 n 的整数排列 A
    # 3) 长度为 n 的整数序列 B
    #
    # 这里将 n 直接作为原程序中的 n，
    # A 生成为 1..n 的一个确定性排列，
    # B 生成为 1..n 的一个确定性排列（同一种构造方式）。
    if n <= 0:
        return

    # 生成确定性的 A：简单循环右移一位的排列
    A = [((i + 1) % n) + 1 for i in range(n)]
    # 生成确定性的 B：简单循环左移一位的排列
    B = [((i - 1) % n) + 1 for i in range(n)]

    REVA = [None] * (n + 1)

    for i in range(n):
        REVA[A[i]] = i + 1

    top = 0
    ANSLIST = []

    for b in B:
        if REVA[b] > top:
            ANSLIST.append(REVA[b] - top)
            top = REVA[b]
        else:
            ANSLIST.append(0)

    for ans in ANSLIST:
        print(ans, end=" ")


if __name__ == "__main__":
    # 示例调用：可按需要修改 n 的大小进行规模化实验
    main(10)