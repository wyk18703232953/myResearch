def main(n):
    # 映射：n -> 原程序中的 n 和 m
    # 这里设定原 n = n，原 m = n
    orig_n = n
    orig_m = n

    count = [0] * orig_n

    # 生成确定性输入数组 a，长度为 m，元素范围在 [1, n]
    # 使用简单的循环模式：1,2,...,n,1,2,... 重复
    a = [(i % orig_n) + 1 for i in range(orig_m)]

    for i in range(orig_m):
        count[a[i] - 1] += 1

    result = min(count)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)