def main(n):
    # n 既作为元素个数，也作为 k（第 k 大元素）
    # 构造一个 n 行、每行 2 个元素的二维数组 a
    # 保持构造规则确定性
    k = n if n > 0 else 1

    a = []
    for i in range(n):
        # 构造两列：
        # 第一列：与 i 相关的值（可有重复，以产生计数效果）
        # 第二列：与 i 相关的值，用于二级排序
        first = (i * 3) // 2     # 随着 i 单调增长，但有重复
        second = (i * 5) % 7     # 有周期性，形成可重复的模式
        a.append([first, second])

    a.sort(key=lambda x: x[1])
    a.sort(reverse=True, key=lambda x: x[0])

    if 1 <= k <= len(a):
        b = a[k - 1]
        result = a.count(b)
    else:
        result = 0

    print(result)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 进行规模实验
    main(10)