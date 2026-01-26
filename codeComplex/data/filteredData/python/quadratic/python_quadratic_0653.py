def main(n):
    # 确定性数据生成：长度为 n 的整数数组
    # a[i] = (i % 10) + 1，避免出现 0 影响原逻辑
    a = [(i % 10) + 1 for i in range(n)]
    a.sort()
    k = 0
    for i in range(n):
        if a[i]:
            k += 1
            for j in range(i + 1, n):
                if a[j] and a[j] % a[i] == 0:
                    a[j] = 0
    # print(k)
    pass
if __name__ == "__main__":
    main(10)