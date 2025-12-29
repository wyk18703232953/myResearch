import random

MOD = 10**9 + 7

def solve(x: int, k: int) -> int:
    if x == 0:
        return 0
    return (pow(2, k + 1, MOD) * x % MOD - (pow(2, k, MOD) - 1)) % MOD

def main(n: int) -> None:
    # 根据规模 n 生成测试数据：
    # 这里将 n 视为生成的数据规模上界，用于随机生成 x, k（都在 [0, n] 内）
    x = random.randint(0, n)
    k = random.randint(0, n)
    ans = solve(x, k)
    print(ans)

if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(10)