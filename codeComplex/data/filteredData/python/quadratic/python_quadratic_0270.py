def main(n):
    # 解释：n 作为规模参数，生成两个长度为 n 的整数列表
    m = n
    list1 = [i for i in range(1, n + 1)]
    list2 = [i for i in range(1, m + 1, 2)]  # 只取奇数，保证有交集但不完全相同

    for i in list1:
        if i in list2:
            print(i, end=' ')
    print()  # 换行，便于多次调用观察


if __name__ == "__main__":
    main(10)