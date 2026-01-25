def main(n):
    # 生成确定性输入：n 和 r，以及长度为 n 的数组 x
    if n <= 0:
        return

    r = 1  # 固定半径，保持算法结构，保证确定性

    # 将规模 n 直接映射为列表长度
    # 使用简单算术构造一个确定性的、分布尚可的序列
    x = [i * 2 for i in range(n)]

    y = [r] * n
    for i in range(n):
        for j in range(i):
            if not (abs(x[i] - x[j]) > 2 * r):
                y[i] = max(
                    y[i],
                    (4 * r ** 2 - (x[i] - x[j]) ** 2) ** 0.5 + y[j]
                )

    for v in y:
        print(v, end=' ')


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小进行时间复杂度实验
    main(10)