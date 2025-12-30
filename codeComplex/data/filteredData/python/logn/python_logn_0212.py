def sum_of_digits(x: int) -> int:
    ans = 0
    for c in str(x):
        ans += int(c)
    return ans


def main(n: int):
    # 生成测试数据：令 s 为 1 到 n 的数位和之一，确保规模相关
    # 这里简单设定 s 为 n 的数位和（若为 0 则设为 1）
    s = sum_of_digits(n)
    if s == 0:
        s = 1

    m = s + 10 - s % 10

    while m - sum_of_digits(m) < s:
        m += 10

    if m <= n:
        result = n - m + 1
    else:
        result = 0

    print(result)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10**6)