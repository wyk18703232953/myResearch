def main(n):
    # n 表示数组长度
    if n <= 0:
        return
    # 确定性生成长度为 n 的数组
    # 元素值分布在 1 到 5 之间
    arr = [(i % 5) + 1 for i in range(n)]
    arr.sort()
    if arr[-1] == 1:
        arr[-1] = 2
    else:
        arr[-1] = 1
    arr.sort()
    print(*arr)


if __name__ == "__main__":
    main(10)