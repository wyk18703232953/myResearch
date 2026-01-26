def main(n):
    # 输入结构：
    # 原程序：
    #   n: 数组长度
    #   a: 长度为 n 的整数数组
    #   m: 查询次数
    #   m 行: 每行一个区间 [l, r]
    #
    # 在重构中：
    #   使用参数 n 同时控制数组长度和查询数量
    #   a[i] = (i * 7 + 3) % (n + 5)  的确定性构造
    #   第 k 个查询为：
    #       l = (k * 2) % n
    #       r = (l + (k * 3 + 1)) % n
    #       且保证 l <= r（若 r < l，则交换）
    if n <= 0:
        return []

    a = [(i * 7 + 3) % (n + 5) for i in range(n)]
    m = n

    parity = 0
    for i in range(n):
        ai = a[i]
        for j in range(i + 1, n):
            if ai > a[j]:
                parity ^= 1

    res = []
    for k in range(m):
        l = (k * 2) % n
        r = (l + (k * 3 + 1)) % n
        if r < l:
            l, r = r, l
        s = r - l + 1
        parity ^= (s * (s - 1) // 2) % 2
        res.append("odd" if parity else "even")
    return res


if __name__ == "__main__":
    # 示例调用：使用 n = 5 进行一次确定性实验
    output = main(5)
    # print("\n".join(output))
    pass