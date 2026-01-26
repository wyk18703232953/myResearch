def sum_of_digits(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

def main(n):
    # 映射：输入规模 n -> 原程序中的 n, s
    # 原程序输入结构为：两个整数 n, s
    # 这里设定：
    #   原 n = n
    #   原 s = n // 2  （确定性构造，随规模线性变化）
    N = n
    S = n // 2

    lo = 0
    hi = N
    x = N + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid - sum_of_digits(mid) >= S:
            if mid < x:
                x = mid
            hi = mid - 1

        else:
            lo = mid + 1
    result = N - x + 1
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)