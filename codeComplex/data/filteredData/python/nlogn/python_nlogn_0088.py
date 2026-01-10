def main(n):
    # 映射含义：
    # n: 列表长度 n，同时 k = max(1, n // 2)
    k = max(1, n // 2)

    lst = []
    for i in range(n):
        # 确定性生成 (p, t)
        # p 在 [1, n//3+1] 内循环，t 为 i 的某种函数
        p = i % (max(1, n // 3)) + 1
        t = (i * 2 + 3) % (n + 5)
        lst.append([p, -t])

    tmp = sorted(lst, key=lambda x: (x[0], x[-1]), reverse=True)[k - 1]
    print(lst.count(tmp))


if __name__ == "__main__":
    main(10)