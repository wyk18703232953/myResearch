def main(n):
    # 解释输入结构：
    # 原程序：
    # n, u
    # e[0..n-1]
    #
    # 将实验规模 n 直接作为数组长度 n
    # 构造一个严格递增的数组 e，保证差值可控
    # 构造一个与 n 有关且不为 0 的 u

    if n < 3:
        # 原算法中有 range(n-2)，n<3 时无有效循环
        # 保持行为：直接打印 -1
        # print(-1)
        pass
        return

    # 构造确定性递增数组 e：
    # 例如：e[i] = i * 3  (步长为 3，保证差值可控)
    e = [i * 3 for i in range(n)]

    # 构造 u：与 n 相关，保证随规模变化
    # 例如：u = n * 2
    u = n * 2

    ans = -1
    k = 2
    for i in range(n - 2):
        while k < n - 1 and e[k + 1] - e[i] <= u:
            k += 1
        if i < k - 1 and e[k] - e[i] <= u:
            ans = max(ans, (e[k] - e[i + 1]) / (e[k] - e[i]))
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：运行若干规模以便实验
    for size in [3, 10, 100, 1000]:
        main(size)