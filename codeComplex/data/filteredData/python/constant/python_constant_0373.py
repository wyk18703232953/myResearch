def main(n):
    # 解释输入映射关系：
    # 这里将 n 映射为四个整数 A, B, C, N，构造方式完全确定性
    # A, B, C 与 N 的关系保证有规模可控且不依赖外部输入
    # 可根据 n 的大小调节构造方式以观察不同规模下的时间开销

    # 为了使规模可控，这里构造：
    # A = n
    # B = 2n
    # C = n // 2
    # N = A + B - C + 1  （保证 D = 1，触发非 -1 输出的情况）
    A = n
    B = 2 * n
    C = n // 2
    N = A + B - C + 1

    D = N - (A + B - C)
    if D <= 0 or C > A or C > B:
        # print('-1')
        pass
        return
    # print(D)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 以做时间复杂度实验
    main(10)