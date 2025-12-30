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
    # 设 k 为与 n 同阶的正整数，保证 k >= 1
    k = max(1, n)

    if n == 1:
        print(0)
    else:
        ans = lower_bound(n, k)
        if ans == k:
            print(-1)
        else:
            print(ans)


if __name__ == "__main__":
    # 示例：调用 main，传入规模 n
    # 使用一个示例规模，可按需要修改
    example_n = 10
    main(example_n)