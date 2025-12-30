def main(n):
    # 根据规模 n 生成测试数据 s
    # 这里假设 s 为 [1, n] 中点，用户可根据需要自行修改生成方式
    s = max(1, n // 2)

    lo, hi = s, n
    ans = n + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        z = sum(map(int, str(mid)))
        if mid >= s + z:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(n - ans + 1)


if __name__ == "__main__":
    # 示例：调用 main(10**6) 或任意规模
    main(1000000)