def main(n):
    # 生成确定性输入：第一行无用，第二行是 n 个整数
    # 这里将列表规模设为 max(1, n)，元素为从 1 到 length 的递增序列
    length = max(1, n)
    a = list(range(1, length + 1))

    # 模拟原程序逻辑
    a = sorted(a)
    if a[-1] == 1:
        result = [*a[:-1], 2]

    else:
        result = [1, *a[:-1]]

    # print(*result)
    pass
if __name__ == "__main__":
    main(5)