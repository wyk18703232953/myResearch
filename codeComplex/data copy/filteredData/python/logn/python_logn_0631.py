def main(n):
    # 生成测试数据：这里构造一个始终有解的 k
    # 原逻辑：对某个 mid，fmid = (mid+1)*(mid+2)/2 - (n - (mid+1))
    # 为了简单，选 mid = n // 2 来生成 k
    mid_test = n // 2
    k = (mid_test + 1) * (mid_test + 2) // 2 - (n - (mid_test + 1))

    left = 0
    right = n - 1

    ans = None
    while left <= right:
        mid = left + (right - left) // 2
        fmid = (mid + 1) * (mid + 2) // 2 - (n - (mid + 1))
        if fmid == k:
            ans = n - 1 - mid
            # 原代码没有 break，会继续二分；这里保持行为一致，不提前退出
        if fmid > k:
            right = mid - 1
        else:  # fmid < k or fmid == k
            left = mid + 1

    if ans is not None:
        # print(ans)
        pass
if __name__ == "__main__":
    # 示例：调用 main，并可在此处调整规模 n
    main(10)