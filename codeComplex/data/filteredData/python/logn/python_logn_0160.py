def findValue(n, m):
    return n * (n + 1) // 2 - m * (m + 1) // 2 - (n - m - 1)


def main(n):
    # 这里将原来的 k 作为规模参数 n 使用
    # 生成测试数据：原代码中有两个参数 n, k
    # 这里约定：令原来的 k = n，原来的 n 随规模生成为 1..maxi 范围内的某个值
    k = n

    # 按原逻辑，maxi 由 k 决定
    maxi = k * (k + 1) // 2 - k + 1

    # 简单生成一个测试用的“目标值” target_n（原来的 n），例如取中间值
    if maxi <= 1:
        target_n = 1

    else:
        target_n = maxi // 2

    # 把原程序中的变量名对齐：
    # 原来的 n -> target_n，原来的 k -> k
    n_val = target_n

    if n_val == 1:
        result = 0
    elif n_val > maxi:
        result = -1

    else:
        begin = 2
        end = k
        MID = 2  # 给个默认值，保证后续使用安全

        while begin <= end:
            mid = (begin + end) // 2
            value = findValue(k, mid)
            if value == n_val:
                MID = mid
                break
            elif value > n_val:
                begin = mid + 1

            else:
                MID = mid
                end = mid - 1

        remaining = n_val - findValue(k, MID)

        if remaining == 0:
            result = k - MID

        else:
            result = k - MID + 1

    # print(result)
    pass
if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)