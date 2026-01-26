def valid(k, mid):
    return (2 * k - mid - 1) * mid // 2 + 1

def binary_search(n, k):
    l, r = 0, k - 1
    while l <= r:
        mid = (l + r) >> 1
        if valid(k, mid) < n:
            l = mid + 1

        else:
            r = mid - 1
    return l

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里设定 k = 2 * n，保证搜索空间随规模增大
    k = 2 * n
    res = binary_search(n, k)
    # print(-1 if res == k else res)
    pass
if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(10)