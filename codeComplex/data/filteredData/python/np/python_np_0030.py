import math

MOD = 1000000007
ANS = [1, 3, 15, 133, 2025, 37851, 1030367, 36362925]

def solve_single(n: int) -> int:
    if n % 2 == 1 and 0 <= n // 2 < len(ANS):
        return ANS[n // 2] * math.factorial(n) % MOD
    return 0

def main(n: int):
    # n 表示要测试的输入规模（从 1 到 n 的所有整数）
    results = []
    for x in range(1, n + 1):
        results.append(solve_single(x))
    for v in results:
        print(v)

if __name__ == "__main__":
    main(10)