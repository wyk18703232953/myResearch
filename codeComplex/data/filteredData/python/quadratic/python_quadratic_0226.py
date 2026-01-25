def main(n):
    if n <= 0:
        return -1

    # 确定性构造输入数据
    # l 为严格递增序列，保证存在可行解
    l = [i for i in range(1, n + 1)]
    # l2 为与下标相关的确定性权值序列
    l2 = [(i * 3) % 10 + 1 for i in range(n)]

    dp_1 = l2.copy()
    INF = 9999999999
    dp_2 = [INF] * n
    dp_3 = [INF] * n

    for i in range(1, n):
        for j in range(i):
            if l[i] > l[j]:
                candidate = dp_1[j] + l2[i]
                if candidate < dp_2[i]:
                    dp_2[i] = candidate

    for i in range(1, n):
        for j in range(i):
            if l[i] > l[j]:
                candidate = dp_2[j] + l2[i]
                if candidate < dp_3[i]:
                    dp_3[i] = candidate

    x = min(dp_3)
    if x == INF:
        return -1
    return x


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小做时间复杂度实验
    result = main(10)
    print(result)