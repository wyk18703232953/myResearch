def main(n):
    # 根据规模 n 生成测试数据
    # 这里构造一个有序数组 a，元素两两不同
    # d 取一个与数列间距同数量级的正整数
    d = 3
    a = [i * 5 for i in range(n)]  # 间隔为 5，保证差值足够分散

    a.sort()
    s = set()
    for i in range(n):
        x = a[i] - d
        left = a[i - 1] if i >= 1 else float('inf')
        if abs(x - left) >= d:
            s.add(x)

        x = a[i] + d
        right = a[i + 1] if i + 1 < n else float('inf')
        if abs(x - right) >= d:
            s.add(x)

    # print(len(s))
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)