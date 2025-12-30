def main(n: int) -> int:
    """
    n: 规模（配对数），会自动生成一组长度为 2*n 的测试数据。
    返回值: 根据原始算法计算得到的 swaps 数。
    """
    # 生成测试数据：构造 1..n，每个数字出现两次，然后打乱。
    # 这里固定使用简单可重复的伪随机打乱，避免依赖随机库。
    a = []
    for x in range(1, n + 1):
        a.append(x)
        a.append(x)

    # 简单的确定性“洗牌”（基于下标交换），不使用 random 模块
    # 使得数组不是已经成对的，以便能产生非零 swaps。
    length = 2 * n
    for i in range(length):
        j = (i * 31 + 7) % length
        a[i], a[j] = a[j], a[i]

    # 原始逻辑：将数组调整为成对相邻，并统计相邻交换次数
    swaps = 0
    for i in range(0, 2 * n, 2):
        if a[i] == a[i + 1]:
            continue

        c = a[i]
        j = i + 2
        while c != a[j]:
            j += 1

        MIN = i + 1
        while j > MIN:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
            swaps += 1

    # 按题意仅返回，不做 print
    return swaps


# 如需本文件直接运行做一个简单演示，可取消下面注释：
# if __name__ == "__main__":
#     print(main(5))