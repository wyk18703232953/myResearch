def main(n):
    # 根据 n 生成测试数据：这里设定 k 为一个与 n 相关的值
    # 为了保证一定有解，这里构造一个 mid0，然后用原公式反推 k
    # mid0 取在 [0, n] 之间
    mid0 = n // 2
    candy = n - mid0
    k = (candy * (candy + 1)) // 2 - mid0

    left = 0
    right = n + 1
    while left < right:
        mid = (left + right) // 2
        candy = n - mid
        total = (candy * (candy + 1)) // 2 - mid
        if total < k:
            right = mid
        elif total > k:
            left = mid + 1
        else:
            print(mid)
            break


if __name__ == "__main__":
    # 这里给一个示例规模 n，可根据需要修改或在外部调用 main(n)
    main(10)