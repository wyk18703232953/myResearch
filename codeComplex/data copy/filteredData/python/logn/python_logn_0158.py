def lower_bound(n, k):
    low = 1
    high = k
    while low < high:
        mid = low + (high - low) // 2
        pipes = mid * k - (mid + 2) * (mid - 1) // 2
        if pipes >= n:
            high = mid

        else:
            low = mid + 1
    return low


def main(n):
    # 根据规模 n 生成测试数据：
    # 假设 k 与 n 同阶，这里简单设置为 k = n
    # 你可以根据需要修改生成策略
    if n <= 0:
        return

    k = n

    if n == 1:
        # print(0)
        pass

    else:
        ans = lower_bound(n, k)
        if ans == k:
            # print(-1)
            pass

        else:
            # print(ans)
            pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)