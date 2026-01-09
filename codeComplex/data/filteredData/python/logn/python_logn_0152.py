def getSum(a):
    return a * (a + 1) // 2

def getSumOfTwo(a, b):
    if a <= 1:
        return getSum(b)
    return getSum(b) - getSum(a - 1)

def solve_single_case(n, k):
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
    """
    n: 规模参数，用于生成测试数据和执行逻辑。
    这里假定原问题中 k 与 n 同级量级，生成一个典型测试：
    令 k = n，调用原逻辑并打印结果。
    """
    # 根据规模 n 生成测试数据，这里简单设定 k = n
    k = n

    ans = solve_single_case(n, k)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：运行一个固定规模，实际使用时由外部调用 main(n)
    main(10)