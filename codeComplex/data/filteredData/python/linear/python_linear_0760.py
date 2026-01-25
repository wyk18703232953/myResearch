def main(n):
    # 生成确定性输入：长度为 n 的整数数组
    # 这里选择简单序列 i * (-1) ** i，既有正又有负，覆盖分支
    a = [i * (-1) ** i for i in range(n)]

    # 原算法逻辑
    for i in range(n):
        if a[i] >= 0:
            a[i] = -a[i] - 1

    if n % 2:
        m = min(a)
        for i in range(n):
            if a[i] == m:
                a[i] = -a[i] - 1
                break

    print(*a)


if __name__ == "__main__":
    # 示例调用，可按需要修改 n 来做规模实验
    main(10)