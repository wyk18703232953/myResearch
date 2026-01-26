def main(n):
    # 根据 n 构造确定性输入：k 和 ls
    # 约束：元素范围在 [0, 255] 之内
    if n <= 0:
        return
    k = max(1, n // 2)
    k = min(k, 256)

    ls = [(i * 7 + 3) % 256 for i in range(n)]

    ar = [-1 for _ in range(256)]

    for e in ls:
        if ar[e] == -1:
            tmp = max(0, e - k + 1)
            i = tmp
            while i <= e:
                if ar[i] != -1 and ar[i] != i:
                    tmp += 1
                    i = tmp
                    continue

                else:
                    while i <= e:
                        ar[i] = tmp
                        i += 1
        # print(ar[e], end=" ")
        pass
    # print()
    pass
if __name__ == "__main__":
    main(10)