def main(n):
    # n 表示数组长度
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性构造：从 1 到 n 的整数序列
    a = [i + 1 for i in range(n)]
    a.sort()

    tot = 0
    d = {}
    for i in range(len(a)):
        if a[i] not in d:
            tot += 1
            for j in range(i + 1, len(a), 1):
                if a[j] % a[i] == 0:
                    d[a[j]] = 1
    # print(tot)
    pass
if __name__ == "__main__":
    # 示例调用
    main(10)