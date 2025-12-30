def main(n):
    # 这里根据 n 生成 k（规模相关的参数），
    # 原逻辑中 k 与 n 无直接输入条件关系，这里做一个合理的设置：
    # 令 k = n，保证搜索空间随规模 n 线性增长。
    k = n

    l, r = -1, k + 1
    while l + 1 < r:
        mid = (l + r) >> 1
        val = (k - mid + 1 + k) * mid // 2 - (mid - 1)
        if val < n:
            l = mid
        else:
            r = mid

    print(-1 if r == k + 1 else r)


if __name__ == "__main__":
    # 示例：调用 main(10) 作为测试
    main(10)