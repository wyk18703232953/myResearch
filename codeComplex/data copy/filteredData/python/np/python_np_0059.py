def factorial(n):
    ans = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        ans *= i
    return ans


def ncr(n, r):
    n = abs(n)
    if r > n:
        return 0
    ans = factorial(n)
    ans = ans // factorial(n - r)
    ans = ans // factorial(r)
    return ans


def main(n):
    """
    n: 生成测试数据的规模参数。
       这里约定：
       - A 固定为全是 '+' 的长度 n 字符串
       - B 固定为全是 '?' 的长度 n 字符串
    """
    A = '+' * n
    B = '?' * n

    QMarks = B.count('?')
    TotalA = A.count('+') - A.count('-')
    TotalB = B.count('+') - B.count('-')

    denominator = 2 ** QMarks

    if QMarks < abs(TotalA - TotalB):
        result = 0.0

    else:
        x = (QMarks - abs(TotalA - TotalB)) // 2
        x += abs(TotalA - TotalB)
        num = ncr(QMarks, x)
        result = num / denominator

    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)