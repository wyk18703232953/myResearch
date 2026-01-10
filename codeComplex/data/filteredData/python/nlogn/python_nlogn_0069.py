def main(n):
    # 生成确定性输入：p 表示数组长度
    p = n
    # 生成一个长度为 p 的整数数组，元素为 p-i 的递减序列
    arr = [p - i for i in range(p)]
    arr.sort(reverse=True)
    d = 0
    for x in arr:
        d += x
    c = 0
    num = 0
    while c <= d / 2 and num < len(arr):
        c += arr[num]
        num += 1
    print(num)


if __name__ == "__main__":
    main(10)