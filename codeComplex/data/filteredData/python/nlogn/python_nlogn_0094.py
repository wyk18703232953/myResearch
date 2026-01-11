def main(n):
    # 映射含义：
    # n 作为数组长度，且需要 n >= 2 才有意义
    if n < 2:
        # print(0)
        pass
        return

    # 确定性生成 a, b
    # 保证 1 <= a <= b <= n-1
    a = 1
    b = n // 2
    if b < 1:
        b = 1
    if b >= n:
        b = n - 1

    # 生成确定性数组：严格递增，便于复现
    arr = [i * 2 for i in range(1, n + 1)]

    arr.sort()
    end_b = arr[b - 1]
    start_a = arr[b]
    if end_b < start_a:
        # print(start_a - end_b)
        pass

    else:
        # print(0)
        pass
if __name__ == "__main__":
    main(10)