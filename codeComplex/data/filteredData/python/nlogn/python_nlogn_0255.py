def search(arr, power):
    lo = 0
    hi = len(arr) - 1
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] <= power:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


def main(n):
    # 生成规模为 n 的测试数据
    # 这里约定 q = n，a 为递增正整数，k 为正整数
    q = n
    a = [i + 1 for i in range(n)]           # 例如: [1, 2, 3, ..., n]
    k = [1 for _ in range(q)]               # 例如: 全 1

    # 前缀和处理
    for i in range(1, n):
        a[i] += a[i - 1]

    power = 0
    for i in range(q):
        power += k[i]
        pos = search(a, power)
        if pos == n - 1:
            print(n)
            power = 0
        elif pos == -1:
            print(n)
        else:
            print(n - pos - 1)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)