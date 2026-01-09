def main(n):
    # 映射含义：
    # n -> 原程序中列表 p 的长度
    # 为保持和原始程序一致，还需要一个 d（常数或随 n 确定性变化）
    #
    # 这里选择 d = max(1, n // 10) 作为确定性构造

    if n <= 0:
        return 0

    d = max(1, n // 10)

    # 构造长度为 n 的数组 p，完全确定性
    # 例如：p[i] = (i * 3) // 2
    p = [(i * 3) // 2 for i in range(n)]

    q = []
    for i in range(len(p) - 1):
        q.append(abs(p[i + 1] - p[i]))

    count = 0
    for k in q:
        if k == 2 * d:
            count += 1
        elif k >= 2 * d:
            count += 2

    result = count + 2
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例调用：可按需修改 n 以做不同规模实验
    main(1000)