def main(n):
    # 解释输入结构：
    # 原程序读取：
    #   n, k
    #   a[0..n-1]
    # 这里将参数 n 映射为原程序的 n（数组长度），k 设为一个与 n 相关的确定性值
    # 测试数据生成：a[i] = (i * 2 - n)，使得数据既有正有负且确定
    if n <= 0:
        print(0.0)
        return

    k = max(1, n // 3)  # 至少为 1，且随 n 线性变化

    a = [i * 2 - n for i in range(n)]

    ans = -1 * 10 ** 9 + 7
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if j - i + 1 >= k:
                ans = max(ans, s / (j - i + 1))
    print(ans)


if __name__ == "__main__":
    main(10)