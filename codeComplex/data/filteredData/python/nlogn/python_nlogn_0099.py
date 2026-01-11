def main(n):
    # 解释输入结构：
    # 原程序读取：
    #   n, p, v = input().split()
    #   x = list(map(int, input().split()))
    # 其中：
    #   - n：列表长度
    #   - p：未使用
    #   - v：索引，在排序后数组中访问 x[v] 和 x[v-1]
    #
    # 为了时间复杂度实验：
    #   - 使用 n 作为列表长度
    #   - 构造确定性数组 x
    #   - 构造确定性索引 v（保证 1 <= v < n）
    #
    # 当 n < 2 时，原逻辑对 x[v] 和 x[v-1] 不合法，这里约定直接返回 0

    if n < 2:
        # print(0)
        pass
        return

    # 构造长度为 n 的确定性数组 x
    # 使用一个简单的线性递增序列，使得排序成本仍然存在，
    # 但值构造完全确定。
    x = [i * 2 for i in range(n)]

    # 构造确定性 v，保证 1 <= v < n
    # 选择中间位置，避免边界问题
    v = n // 2
    if v == 0:
        v = 1
    if v >= n:
        v = n - 1

    # 原逻辑：排序后取差值
    x.sort()
    result = x[v] - x[v - 1]
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小进行时间复杂度实验
    main(10)