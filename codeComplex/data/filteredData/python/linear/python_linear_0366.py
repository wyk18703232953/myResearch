def main(n):
    # 映射规则：
    # 原程序有 n, m 两个参数以及两个长度分别为 n 和 m 的数组
    # 这里将传入的 n 作为原程序的 n
    # 为了控制规模，令 m = n
    # arr1 和 arr2 都是长度为 n 的确定性数组

    m = n

    # 构造确定性数组：
    # arr1 为递增序列 [0, 2, 4, ..., 2*(n-1)]
    # arr2 为递增序列 [1, 3, 5, ..., 2*(n-1)+1]
    arr1 = [2 * i for i in range(n)]
    arr2 = [2 * i + 1 for i in range(m)]

    j = 0
    for i in range(n):
        if j < m and arr2[j] >= arr1[i]:
            j += 1
    print(j)


if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的大小做时间复杂度实验
    main(10)