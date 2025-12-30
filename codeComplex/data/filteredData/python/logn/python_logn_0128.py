import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 原程序依赖 n, k 且需要满足有解的情况，为方便测试，
    # 这里构造一个总能找到解的 (n, k)。
    #
    # 原公式：
    #   val(mid) = ((k-1)*k//2) - ((mid-1)*mid//2) + 1
    # 对于 mid = k-1，有：
    #   val(k-1) = k
    # 因此如果我们令 n = k，则 mid = k-1 必为一个解。
    #
    # 所以给定输入规模 n，我们直接设置：
    #   k = n
    # 这样原代码在 mid = k-1 时必有 val == n。

    if n <= 0:
        # 对于非正 n，原问题语义不清，这里直接返回，不做计算
        return

    k = n
    start = k - 1
    end = 1

    def bsearch(start, end):
        if start < end:
            return start
        else:
            mid = start - (start - end) // 2
            val = ((k - 1) * k // 2) - ((mid - 1) * mid // 2) + 1
            if val == n:
                return mid
            elif val > n:
                end = mid + 1
            else:
                start = mid - 1
            return bsearch(start, end)

    ans = bsearch(start, end)

    if ans == 0:
        print(-1)
    elif n == 1:
        print(0)
    else:
        print(k - ans)


if __name__ == "__main__":
    # 示例：按不同规模调用 main(n)
    for test_n in [1, 2, 5, 10, 20]:
        print(f"n = {test_n} -> ", end="")
        main(test_n)