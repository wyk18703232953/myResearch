import math


def cnt_digit_order(X):
    res = 0
    if X == 0:
        return 0
    for i in range(1, X + 1):
        res += i * (9 * pow(10, i - 1))
    return res


def solve(k):
    L = -1
    leftcnt = 0
    for length in range(1, 100):
        if cnt_digit_order(length - 1) < k <= cnt_digit_order(length):
            L = length
            leftcnt = k - cnt_digit_order(length - 1)
            break

    M = str(math.ceil(leftcnt / L) + (10 ** (L - 1) - 1))
    leftcnt -= 1
    leftcnt %= L
    return M[leftcnt]


def main(n):
    # 将 n 映射为原程序中的 k
    # 这里选用简单的确定性映射：k = max(1, n)
    k = max(1, n)
    ans = solve(k)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：使用一个固定的 n 作为规模参数
    main(10)