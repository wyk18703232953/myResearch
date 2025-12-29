def getSum(a):
    return a * (a + 1) // 2

def getSumOfTwo(a, b):
    if a <= 1:
        return getSum(b)
    return getSum(b) - getSum(a - 1)

def solve(n, k):
    if n == 1:
        return 0
    if n <= k:
        return 1
    if getSum(k - 1) < n - 1:
        return -1

    n -= 1
    k -= 1
    left, right = 1, k
    while left < right:
        mid = (left + right) // 2
        sum1 = getSumOfTwo(mid, k)
        if sum1 == n:
            return k - mid + 1
        if sum1 > n:
            left = mid + 1
        else:
            right = mid
    return k - left + 2

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里设定 k 与 n 同阶，使得大部分情况下可行：
    # 1) n = 1 特殊情况；2) 一般情形 k 取 n 或 2n 确保 getSum(k-1) 足够大
    if n <= 2:
        k = max(1, n)
    else:
        k = 2 * n  # 保证 sum(1..k-1) >= n-1，避免大量 -1 情况

    ans = solve(n, k)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)