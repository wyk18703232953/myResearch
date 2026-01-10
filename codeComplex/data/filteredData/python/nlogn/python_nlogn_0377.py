def main(n):
    # 映射：n 作为数组长度，k 为一个与 n 相关的确定性值
    k = n // 3 + 1
    arr = [(i * 2 + (i // 3)) % (5 * n + 7) for i in range(n)]
    arr.sort()
    c = n
    j = 0
    for x in arr:
        while x > arr[j]:
            if x - arr[j] <= k:
                c -= 1
            j += 1
            if j >= n:
                break
        if j >= n:
            break
    print(c)


if __name__ == "__main__":
    main(10)