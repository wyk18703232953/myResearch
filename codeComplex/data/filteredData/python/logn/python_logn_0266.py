import random

M = 1000000007

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

def main(n):
    # 根据规模 n 生成测试数据，这里令:
    #   x 在 [0, 10^9] 区间随机
    #   使用传入的 n 作为原代码中的 n
    x = random.randint(0, 10**9)

    ans = pwr(2, n + 1, M) * x
    ans %= M
    ans = ans - pwr(2, n, M) + 1
    ans = (ans + M) % M
    if x == 0:
        ans = 0

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)