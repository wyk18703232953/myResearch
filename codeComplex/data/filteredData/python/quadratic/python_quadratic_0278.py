def main(n):
    # 映射：n 表示每个数组的长度
    length = max(1, n)

    # 确定性生成 arr1 和 arr2
    arr1 = [i for i in range(1, length + 1)]
    arr2 = [i * 2 for i in range(1, length + 1)]

    # 保持原有逻辑：输出两个数组的交集元素（按原程序的双重循环顺序）
    output = []
    for first in arr1:
        for second in arr2:
            if first == second:
                output.append(str(first))

    if output:
        print(" ".join(output))
    else:
        print()


if __name__ == "__main__":
    # 示例：可调整 n 观测规模变化
    main(10)