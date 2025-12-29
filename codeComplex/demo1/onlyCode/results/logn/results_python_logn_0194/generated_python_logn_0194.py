def main(n):
    # 生成测试数据：n 给定，随机或固定生成 s
    # 这里用一个简单可控的方式：令 s 为 n 的一半（向下取整），并确保 s >= 0
    s = max(0, n // 2)

    low = s
    high = n + 1
    ans = n + 1

    # 对照原逻辑的二分查找
    while low <= high:
        mid = (low + high) // 2
        ss = sum(int(c) for c in str(mid))
        if mid - ss < s:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1

    # 原程序输出的是 n - ans + 1
    result = n - ans + 1
    print(result)


if __name__ == "__main__":
    # 示例运行：可根据需要修改 n
    main(1000)