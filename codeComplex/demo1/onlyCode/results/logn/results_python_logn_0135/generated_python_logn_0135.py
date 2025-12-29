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
    # 约定：k 为不小于 n 的整数，取 k = 2 * n 以保证有搜索空间
    k = max(1, 2 * n)

    res = binary_search(n, k)
    return -1 if res == k else res

if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    print(main(10))