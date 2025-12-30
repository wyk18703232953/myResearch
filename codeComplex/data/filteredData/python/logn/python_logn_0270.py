import random

MOD = 10**9 + 7

def my_pow(a, n, m):
    if n == 0:
        return 1
    ans = my_pow(a, n // 2, m)
    if n % 2 == 0:
        return ans * ans % m
    else:
        return (ans * ans * a) % m

def solve(x, k):
    if x == 0:
        return 0
    mod = MOD
    x *= 2
    ans = (x - 1) * my_pow(2, k, mod) + 1
    ans %= mod
    ans += 2 * mod
    return ans % mod

def main(n):
    # 根据规模 n 生成测试数据
    # 这里生成 n 组 (x, k)，并打印对应答案
    random.seed(0)
    for _ in range(n):
        # x, k 的规模可以根据需要调整，这里给出一个示例：
        x = random.randint(0, 10**9)
        k = random.randint(0, 10**9)
        print(solve(x, k))

if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)