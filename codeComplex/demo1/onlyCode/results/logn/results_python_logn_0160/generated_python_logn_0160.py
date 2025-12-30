def findValue(n, m):
    return n * (n + 1) // 2 - m * (m + 1) // 2 - (n - m - 1)


def solve(n, k):
    maxi = k * (k + 1) // 2 - k + 1

    if n == 1:
        return 0
    elif n > maxi:
        return -1
    else:
        begin = 2
        end = k
        MID = 2  # default initialization, will be updated in loop

        while begin <= end:
            mid = (begin + end) // 2
            value = findValue(k, mid)

            if value == n:
                MID = mid
                break
            elif value > n:
                begin = mid + 1
            else:
                MID = mid
                end = mid - 1

        remaining = n - findValue(k, MID)

        if remaining == 0:
            return k - MID
        else:
            return k - MID + 1


def main(n):
    """
    根据规模 n 生成测试数据并返回对应结果。
    这里约定：
    - k 至少为 2
    - 为了保证有意义，令 k = n（可根据需要更改生成规则）
    """
    k = max(2, n)
    return solve(n, k)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    print(main(10))