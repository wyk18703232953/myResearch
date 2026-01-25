def main(n):
    # n 表示每个数组的长度，生成两个长度为 n 的数组
    if n <= 0:
        return

    # 确定性生成 arr1 和 arr2
    arr1 = [i % (n // 2 + 1) for i in range(n)]
    arr2 = [(i * 2 + 1) % (n // 2 + 1) for i in range(n)]

    result = sorted(
        [x for x in arr2 if x in arr1],
        key=lambda k: arr1.index(k)
    )
    print(*result)


if __name__ == "__main__":
    main(10)