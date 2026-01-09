def main(n):
    # n 作为序列和匹配列表的长度
    m = n

    # 生成确定性的字符串序列 seq 和 fp
    # seq: ["0", "1", ..., str(n-1)]
    seq = [str(i) for i in range(n)]
    # fp: ["k", "k+1", ..., str(k + m - 1)]，k 确定性为 n//2
    k = n // 2
    fp = [str(k + i) for i in range(m)]

    # 原始算法逻辑
    checklist = []
    for number in seq:
        if number in fp:
            checklist.append(number)

    # 输出结果
    if checklist:
        # print(" ".join(checklist))
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    main(10)