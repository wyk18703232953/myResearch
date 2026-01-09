def main(n):
    # 解释输入结构映射：
    # 原程序输入：
    #   n, m, k
    #   arr (长度 n)
    #
    # 为了可规模化、确定性和保持语义：
    #   将 main(n) 中的 n 作为原输入 n 的规模，即数组长度
    #   m 与 k 选择与 n 有确定性关系
    #   构造一个长度为 n 的数组 arr，保持递增以匹配原逻辑使用场景
    
    if n <= 0:
        # 无有效数据，直接输出 0
        # print(0)
        pass
        return

    # 确定性构造 m, k
    # m 为原数组长度 n（扩容后长度为 2m）
    m = n
    # k 选取一个与 n 有关但不少于 1 的步长系数
    k = max(1, n // 5)

    # 构造确定性的递增数组 arr，模拟原题“页面索引”场景：
    # 例如：arr[i] = i*2 + 1，即严格递增的奇数序列
    arr = [i * 2 + 1 for i in range(n)]

    # 下面保留原核心算法逻辑，仅移除 input 并使用上面构造的数据
    arr = list(arr)
    arr += [0] * m
    ans = 0
    pos = 0
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
    # 示例调用，可按需修改 n 进行时间复杂度实验
    main(10)