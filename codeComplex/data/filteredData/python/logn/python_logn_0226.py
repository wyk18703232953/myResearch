def dsum(n):
    return sum(int(c) for c in str(n))

def main(n):
    # 根据规模 n 生成测试数据：
    # 令 s 为 n 的一半的数位和差值附近的某个值，保证有一定数量解
    # 原题含义：给定 n, s，求满足 x - dsum(x) >= s 的 x ∈ [1, n] 的个数
    # 这里构造 s
    s = max(0, n // 2 - dsum(n // 2))

    l = 1
    r = n
    while l <= r:
        mid = (l + r) // 2
        delta = mid - dsum(mid)
        if delta >= s:
            r = mid - 1
        else:
            l = mid + 1
    print(n - l + 1)

if __name__ == "__main__":
    # 示例：可更改为任意规模
    main(10**6)