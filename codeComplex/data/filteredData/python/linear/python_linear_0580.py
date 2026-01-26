def main(n):
    # 由 n 确定性生成原程序的两个输入：N 和 S
    # 映射规则：N = n，S = n * (n + 1) // 2
    N = n
    s = n * (n + 1) // 2

    cnt = 0
    for i in range(N, 0, -1):
        cnt += s // i
        s %= i
    # print(cnt)
    pass
if __name__ == "__main__":
    main(10)