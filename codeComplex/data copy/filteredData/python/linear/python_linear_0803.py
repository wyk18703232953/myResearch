def main(n):
    # n 作为数组长度规模参数
    if n <= 0:
        return 0
    # 构造输入结构：
    # 原程序第一行: n[0], n[1], n[2]
    # 这里令:
    #   n0 = n
    #   n1 = n
    #   k  = max(1, n // 3)  保证随规模变化但确定
    n0 = n
    n1 = n
    k = max(1, n // 3)  # divisor
    params = [n0, n1, k]

    # 原程序第二行: 数组 a，长度为 n[1]
    # 使用简单确定构造: a[i] = i * 2 + (i // 3)
    a = [i * 2 + (i // 3) for i in range(n1)]

    # 保持原算法逻辑
    k = params[2]
    ans = 0
    dele = 1
    i = 0
    while i < params[1]:
        count = 1
        while (i + count) < params[1] and (a[i + count] - dele) // k == (a[i] - dele) // k:
            count += 1
        ans += 1
        dele += count
        i += count

    return ans


if __name__ == "__main__":
    # 示例调用
    for test_n in [1, 5, 10, 100]:
        # print(test_n, main(test_n))
        pass