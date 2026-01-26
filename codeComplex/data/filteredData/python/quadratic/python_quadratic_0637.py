def main(n):
    # n 表示列表长度
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性生成长度为 n 的整数列表
    # 模式：l[i] = i + 1，保证正整数且有丰富的整除关系
    l = sorted([i + 1 for i in range(n)])

    seen = [False] * n
    res = 0
    for i in range(n):
        if seen[i]:
            continue
        res += 1
        for j in range(i, n):
            seen[j] |= (l[j] % l[i] == 0)
    # print(res)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要调整 n 规模
    main(10)