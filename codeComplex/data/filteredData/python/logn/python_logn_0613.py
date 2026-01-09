import math

def valid(n, k, c1, c2):
    if c1 > n:
        return c2
    elif c2 > n:
        return c1
    ans_one = ((n - c1) * (n - c1 + 1) // 2) - c1
    if ans_one == k:
        return c1
    return c2


def f(n, k):
    b2 = (2 * n + 3)
    delta = int(math.sqrt(8 * n + 8 * k + 9))
    return valid(n, k, (b2 + delta) // 2, (b2 - delta) // 2)


def main(n):
    # 规模解释：
    # 将 n 视为原程序里的 n，k 由 n 确定性构造
    # 这样输入规模就是单个整数 n，且数据可规模化、可重复
    original_n = n
    k = n * (n + 1) // 4  # 确定性构造 k，随 n 规模增长
    result = f(original_n, k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 进行时间复杂度实验
    main(10)