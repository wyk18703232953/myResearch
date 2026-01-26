def main(n):
    if n <= 0:
        # print(0)
        pass
        return

    # 生成确定性输入：长度为 n 的整数列表 a
    # 这里选择简单的线性构造，便于规模化与重复实验
    a = [(i * 2 + 1) % (n + 3) for i in range(n)]

    khat = [0] * n
    ted = 0
    khat[0] = 1

    for i in range(1, len(khat)):
        khat[i] = max(khat[i - 1], a[i] + 1)

    for i in range(len(khat) - 2, -1, -1):
        if khat[i] < khat[i + 1] - 1:
            khat[i] = khat[i + 1] - 1
        ted = ted + (khat[i] - (a[i] + 1))

    ted = ted + (khat[n - 1] - (a[n - 1] + 1))
    # print(ted)
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的大小进行实验
    main(10)