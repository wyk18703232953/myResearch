import random

def main(n):
    # 1. 生成测试数据
    # 生成一个长度为 n 的数字串 a_str（不以 0 开头）
    if n <= 0:
        return 0
    first_digit = str(random.randint(1, 9))
    other_digits = [str(random.randint(0, 9)) for _ in range(n - 1)]
    a_str = first_digit + ''.join(other_digits)
    
    # 生成上界 b：保证位数不少于 n，避免过小导致结果为 0
    # 这里让 b 在 [10^(n-1), 10^n - 1] 范围内
    low = 10**(n - 1) if n > 1 else 0
    high = 10**n - 1
    b = random.randint(low, high)

    # 2. 原逻辑实现
    a = list(a_str)
    a.sort(reverse=True)
    ans = ''
    while a:
        for i in range(len(a)):
            temp = ''
            x = ans + a[i] + temp.join(sorted(a[:i] + a[i+1:]))
            if int(x) <= b:
                ans += a[i]
                a = a[:i] + a[i+1:]
                break

    # 输出结果（与原程序行为一致，只打印最终整数）
    print(int(ans))


if __name__ == "__main__":
    # 示例：调用 main，n 为数字串长度规模
    main(5)