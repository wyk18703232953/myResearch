import random

MOD = 10 ** 9 + 7

def solve_one(x, k):
    if x == 0:
        return 0
    return (pow(2, k + 1, MOD) * x % MOD - (pow(2, k, MOD) - 1)) % MOD

def main(n):
    """
    n：测试数据规模，生成 n 组 (x, k) 并依次计算输出。
    """
    random.seed(0)  # 固定种子，保证复现性
    results = []
    for _ in range(n):
        # 生成测试数据，可根据需要调整范围
        x = random.randint(0, 10**9)
        k = random.randint(0, 10**9)
        results.append(solve_one(x, k))
    for ans in results:
        print(ans)

if __name__ == "__main__":
    # 示例：运行 5 组测试
    main(5)