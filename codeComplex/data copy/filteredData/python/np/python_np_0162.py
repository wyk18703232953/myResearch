def main(n):
    # 映射：n 作为数组长度
    size = max(1, n)

    # 确定性构造参数 l, r, x
    # 让 r 足够大以避免所有子集都被过滤掉
    l = size  # 至少要选到一些元素
    r = size * (size + 1) // 2  # 1..size 的和
    x = max(1, size // 4)

    # 构造确定性数组 a：1, 2, 3, ..., size
    a = [i + 1 for i in range(size)]

    ans = 0
    # 原逻辑枚举子集：使用 0..(2**n - 1)
    for mask in range(1, 2 ** size):
        # 构造与原程序相同的二进制字符串形式
        j = bin(mask)[2:]
        if len(j) < size:
            j = '0' * (size - len(j)) + j

        c = 0
        temp = []
        for k in j:
            if k == '1':
                temp.append(a[c])
            c += 1

        s = sum(temp)
        if len(temp) >= 2 and l <= s <= r and (max(temp) - min(temp)) >= x:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：以 n=10 作为规模调用
    main(10)