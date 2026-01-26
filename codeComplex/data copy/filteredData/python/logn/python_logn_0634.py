def main(n):
    # 解释原始输入结构：原程序从 input() 读取两个整数 n, k
    # 在这里我们将实验规模参数 n 作为原来的 n，
    # 并构造一个确定性的 k，随规模变化但不依赖外部输入。
    #
    # 选择一个与 n 成二次量级同阶的 k，保证算法路径有意义。
    # 这里取 k = n * (n + 1) // 4（当 n 足够大时介于 0 和 n(n+1)/2 之间）。
    k = n * (n + 1) // 4

    def split_k(x):
        t = x + 1
        addition = t * (t + 1) // 2
        return (addition - (n - x - 1) - k, n - x - 1)

    j = 0
    while split_k(j)[0] != 0 and j < n:
        j += 1

    # 如果在 [0, n-1] 范围内没有找到使 split_k(j)[0] == 0 的 j，
    # 原代码会无限循环；为了实验可扩展性，这里限定 j < n，
    # 若未找到则按照原意返回最后一次 split_k(j)[1] 的值。
    result = split_k(j)[1]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 以做时间复杂度实验
    main(10)