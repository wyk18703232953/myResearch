def main(n):
    # 解释规模含义：
    # n 表示原程序中的 m（即原数组长度），同时我们也设 k 与 m 相关
    # 为了保证可扩展性和确定性：
    #   m = n
    #   k = max(1, n // 3)  避免 k 为 0
    #
    # arr 的生成逻辑：
    #   原程序中 arr 初始长度为 m，之后补 m 个 0
    #   这里构造一个非递减正整数数组，方便分页逻辑：
    #     arr[i] = i + 1
    #   当 n 较小时，也能保持行为稳定
    #
    # 若需要改变输入模式，只需保证 arr 的生成完全由 n 决定且确定性。

    if n <= 0:
        # 没有有效页面时，答案显然为 0
        # print(0)
        pass
        return

    m = n
    k = max(1, n // 3)

    # 原始输入结构：
    # n, m, k
    # arr（长度 m）
    # 这里 n、m、k 已通过 n 决定，arr 由 n 决定
    arr = [i + 1 for i in range(m)]

    # 原程序中：arr + [0]*m
    arr += [0] * m

    ans = 0
    pos = 0
    # 核心逻辑保持不变
    while arr[pos] != 0:
        page = (arr[pos] - pos - 1) // k
        tmp = 1
        for i in range(1, k):
            if pos + i >= 2 * m - 1:
                break
            if (arr[pos + i] - pos - 1) // k == page:
                tmp += 1

            else:
                break
        pos += tmp
        ans += 1

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：可以根据需要修改 n 进行规模实验
    main(10)