def main(n):
    # 映射规则：
    # n >= 2 时，将输入解释为：
    #   原程序中的 n' = n
    #   原程序中的 m' = n
    #   A 长度为 m'，元素在 [1, n'] 内确定性生成
    # n <= 1 时，退化为最小可行规模 n' = 1, m' = 1
    if n <= 1:
        orig_n = 1
        orig_m = 1

    else:
        orig_n = n
        orig_m = n

    # 确定性生成 A：长度为 orig_m，元素在 [1, orig_n]
    # 使用简单算术构造：((i % orig_n) + 1)
    A = [((i % orig_n) + 1) for i in range(orig_m)]

    L = [0] * orig_n
    for i in range(orig_m):
        L[A[i] - 1] += 1
    result = min(L)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)