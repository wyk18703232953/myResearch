def main(n):
    if n < 3:
        # print("NO")
        pass
        return

    # 构造长度为 n 的确定性整数序列
    # 示例：严格“山峰形”序列，前半部分递增，后半部分递减
    mid = n // 2
    a = list(range(1, mid + 2))  # 1,2,...,mid+1
    a += list(range(mid, 0, -1))  # mid,mid-1,...,1
    a = a[:n]  # 截断或正好长度为 n

    c = 0
    for i in range(1, n - 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            c += 1
        if a[i] == a[i - 1] or a[i] == a[i + 1]:
            # print('NO')
            pass
            return
        if a[i] <= a[i - 1] and a[i] <= a[i + 1]:
            # print('NO')
            pass
            return
    if c > 1:
        # print('NO')
        pass

    else:
        # print('YES')
        pass
if __name__ == "__main__":
    main(10)