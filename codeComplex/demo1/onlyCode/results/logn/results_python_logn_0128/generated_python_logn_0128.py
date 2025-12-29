def main(n):
    """
    按原逻辑：给定规模 n，自动生成 k，并输出结果。
    这里选择 k = n（可根据需要调整为其他关于 n 的函数）。
    """
    k = max(1, n)  # 保证 k >= 1

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


# 示例：运行 main(10)
if __name__ == "__main__":
    main(10)