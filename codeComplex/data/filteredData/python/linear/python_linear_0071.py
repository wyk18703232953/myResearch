def main(n):
    # 输入结构分析：
    # 原程序读取：
    # 1) 第一行：n, s
    # 2) 接着 n 行：每行两个整数
    #
    # 这里将 n 用作“数组长度”，并为每个 n 构造一组确定性数据。
    #
    # 规模约定：
    # - 数组长度 = n
    # - s 取一个与 n 线性相关的确定性值，例如 s = 10 * n
    #
    # 数组构造：
    # - 原程序按第 0 列降序排序，因此这里先构造，再交给排序处理
    # - 构造规则（完全确定性）：
    #   arr[i][0] = (n - i)          # 保证初始是严格递减的，排序后仍为从大到小
    #   arr[i][1] = (i * i) // 2     # 一个随 i 增长的确定性序列

    if n <= 0:
        return 0

    s = 10 * n
    arr = [[n - i, (i * i) // 2] for i in range(n)]

    arr = sorted(arr, reverse=True, key=lambda x: x[0])
    ans, c = 0, 0

    for i in range(n):
        if i != 0:
            c = arr[i - 1][0]
        if i == 0:
            ans = ans + s - arr[i][0]
        else:
            ans = ans + c - arr[i][0]
        if arr[i][1] >= ans:
            ans = ans + (arr[i][1] - ans)

    ans = ans + arr[n - 1][0]
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：使用若干不同规模调用 main
    for size in [1, 2, 5, 10]:
        main(size)