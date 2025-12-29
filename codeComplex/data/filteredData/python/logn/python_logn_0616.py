def main(n):
    """
    n 作为规模参数，用来生成 tot 和 choc 测试数据。
    这里示例生成方式：
    - tot = n
    - choc = n // 3
    """
    tot = n
    choc = n // 3

    bg = 1
    end = tot

    while True:
        mid = (bg + end) // 2  # 用整除保持整数
        add = mid * (mid + 1) // 2
        sub = tot - mid
        diff = add - sub

        if diff == choc:
            print(int(sub))
            break
        if diff < choc:
            bg = mid + 1
        else:
            end = mid - 1


if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)