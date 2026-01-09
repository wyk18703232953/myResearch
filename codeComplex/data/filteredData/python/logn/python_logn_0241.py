def digit_sum(n):
    cnt = 0
    while n:
        cnt += n % 10
        n //= 10
    return cnt


def bsearch(low, high, s):
    h = high
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if mid - digit_sum(mid) >= s:
            ans = mid
            high = mid - 1

        else:
            low = mid + 1
    if ans == -1:
        return 0

    else:
        return h - ans + 1


def main(n):
    # 根据规模 n 生成测试数据
    # 原程序需要 n, s，这里 n 由参数给出，s 生成为与 n 相关的值
    # 示例：取 s 为 n 的一半（向下取整）
    s = n // 2

    cnt = 0
    cnt += bsearch(1, n, s)
    # print(cnt)
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(10**12)