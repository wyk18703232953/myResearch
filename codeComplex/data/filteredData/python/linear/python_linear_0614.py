def main(n):
    # n 表示数组中可能出现的最大值，也是 arr 和 brr 的长度
    if n <= 0:
        return

    # 构造 arr：1..n 的一个排列，这里用简单的“反转”来保证确定性
    # arr[i] 的值是 n-i，即 [n, n-1, ..., 1]
    arr = [n - i for i in range(n)]

    numb = [0 for _ in range(n + 1)]
    for i in range(len(arr)):
        numb[arr[i]] = i + 1

    # 构造 brr：1..n 的顺序数组
    brr = [i + 1 for i in range(n)]

    ind = 0
    outputs = []
    for c in brr:
        total = 0
        num = numb[c]
        if num > ind:
            total = num - ind
            ind = num
        outputs.append(str(total))
    print(" ".join(outputs))


if __name__ == "__main__":
    # 示例：使用 n=10 进行一次确定性运行
    main(10)