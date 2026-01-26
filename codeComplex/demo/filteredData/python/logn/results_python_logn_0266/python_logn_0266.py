def pwr(a, n, m):
    if n == 0:
        return 1
    ans = pwr(a, n // 2, m)
    ans = ans * ans
    ans %= m
    if n % 2 == 1:
        return (ans * a) % m

    else:
        return ans

M = 1000000007

def core_logic(x, n):
    ans = pwr(2, n + 1, M) * x
    ans %= M
    ans = ans - pwr(2, n, M) + 1
    ans = (ans + M) % M
    if x == 0:
        ans = 0
    return ans

def main(n):
    # 由规模参数 n 生成确定性输入 x, exp_n
    # 这里将原来的 n 映射为 exp_n = n，x 为与 n 相关的确定性值
    exp_n = n
    x = (n * 1234567) % M
    result = core_logic(x, exp_n)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的大小做时间复杂度实验
    main(10)