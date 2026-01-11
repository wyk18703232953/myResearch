def main(n):
    # n 表示序列长度
    if n <= 0:
        return

    # 确定性生成序列：包含重复最小值以及其他值
    # 生成方式：前 n//3 个为 1，后面为从 2 开始递增
    sequence = []
    for i in range(n):
        if i < n // 3:
            sequence.append(1)

        else:
            sequence.append(2 + (i - n // 3))

    firstOrderStatistics = min(sequence)
    if sequence.count(firstOrderStatistics) == len(sequence):
        # print("NO")
        pass

    else:
        sequence = sorted(sequence)
        secondOrderStatistics = sequence[0]
        for i in sequence:
            if i > secondOrderStatistics:
                secondOrderStatistics = i
                break
        # print(secondOrderStatistics)
        pass
if __name__ == "__main__":
    main(10)