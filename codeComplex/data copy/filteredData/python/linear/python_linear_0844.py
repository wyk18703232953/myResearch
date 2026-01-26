def main(n):
    # n 表示数组长度
    if n <= 0:
        return "NO"

    # 构造一个“先非降后非增”的确定性序列，保持原算法语义
    # 例如：严格上升到中点，再严格下降
    peak_index = n // 2
    a = [i if i <= peak_index else 2 * peak_index - i for i in range(n)]

    i = a.index(max(a))
    v = True
    for j in range(0, i):
        if a[j] > a[j + 1]:
            v = False
    for j in range(i, n - 1):
        if a[j] < a[j + 1]:
            v = False
    result = "YES" if v else "NO"
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例：以 n = 10 运行一次
    main(10)