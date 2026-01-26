def main(n):
    if n <= 0:
        return
    # 生成确定性输入数据
    # l 为严格递增序列，以保证存在解
    l = [i + 1 for i in range(n)]
    # l2 为与下标相关的确定性权值
    l2 = [(i * 3 + 1) % 100 + 1 for i in range(n)]

    dp_1 = l2.copy()
    INF = 9999999999
    dp_2 = [INF] * n
    dp_3 = [INF] * n

    for i in range(1, n):
        for j in range(i):
            if l[i] > l[j]:
                dp_2[i] = min(dp_2[i], dp_1[j] + l2[i])

        for j in range(i):
            if l[i] > l[j]:
                dp_3[i] = min(dp_3[i], dp_2[j] + l2[i])

    x = min(dp_3)
    if x == INF:
        # print(-1)
        pass

    else:
        # print(x)
        pass
if __name__ == "__main__":
    main(10)