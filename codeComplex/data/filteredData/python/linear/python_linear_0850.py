def main(n):
    # 构造确定性输入：长度为 n 的排列 a，元素为 1..n，采用简单的映射
    # 例如：a[i] = (i * 2) % n + 1，保证是一个排列（当 n 为奇数时为完全置换；
    # 为了普适，这里构造一个固定的排列方式）
    a = list(range(1, n + 1))
    # 做一个确定性的变换：将前半段反转，后半段保持
    mid = n // 2
    a = a[:mid][::-1] + a[mid:]

    rev = [-1] * (n + 1)
    for i, j in enumerate(a):
        rev[j] = i

    mx = max(a)

    # [l, r]
    l = a.index(mx)
    r = l

    for i in range(n - 1, 0, -1):
        idx = rev[i]
        if idx == l - 1:
            l -= 1
        elif idx == r + 1:
            r += 1

        else:
            # print('NO')
            pass
            return
    # print('YES')
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小进行实验
    main(10)