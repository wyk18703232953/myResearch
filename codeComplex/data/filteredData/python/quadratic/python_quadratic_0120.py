def main(n):
    if n <= 0:
        return

    # 构造与原程序等价的输入结构：
    # 第一行: "n useless"
    useless = n + 1

    # 第二行: n 个整数的数组 arr
    # 这里生成一个确定性的数组：
    # 对于索引 i (0-based)，arr[i] = (i % n) + 1
    # 这样 arr 中必然包含 1..n 的所有值
    arr = [(i % n) + 1 for i in range(n)]

    # 原算法逻辑
    for x in range(1, n + 1):
        if x not in arr:
            # print(0)
            pass
            break

    else:
        # print(arr.count(min(arr, key=lambda x: arr.count(x))))
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要更改 n
    main(10)