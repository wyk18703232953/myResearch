def main(n):
    # 映射：原代码中 n 为第一个输入，本重构中 n 既作为原 n，又作为 m
    orig_n = n
    orig_m = n

    # 确定性生成 arr1 和 arr2
    # arr1: 递增序列，从 1 到 orig_n
    arr1 = [i + 1 for i in range(orig_n)]
    # arr2: 每个元素是 (2*i) // 3，长度为 orig_m
    arr2 = [(2 * i) // 3 for i in range(orig_m)]

    j = 0
    for i in range(orig_n):
        if j < orig_m and arr2[j] >= arr1[i]:
            j += 1
    # print(j)
    pass
if __name__ == "__main__":
    main(10)