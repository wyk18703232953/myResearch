def case(mid: int) -> int:
    res = 0
    for x in str(mid):
        res += int(x)
    return res


def main(n: int):
    # 根据规模 n 生成测试数据，这里构造 s，使得问题有一定难度
    # 原始问题：统计在 [0, n] 中满足 x - sum_digits(x) >= s 的整数个数
    # 这里令 s = n // 2 作为示例（可按需要调整生成规则）
    s = n // 2

    i, j = 0, n
    while i + 1 < j:
        mid = (i + j) // 2
        if mid - case(mid) < s:
            i = mid

        else:
            j = mid

    if i - case(i) >= s:
        # print(n - i + 1)
        pass

    else:
        if j == n:
            if j - case(j) >= s:
                # print(1)
                pass

            else:
                # print(0)
                pass

        else:
            # print(n - j + 1)
            pass
if __name__ == "__main__":
    # 示例：调用 main(1000000)
    main(1000000)