import random
import sys

MOD = 1_00_00_00_007
MA = float("inf")
MI = float("-inf")

def solve(a, b):
    """
    原逻辑：
    给定区间 [a, b]，寻找三个连续整数 x, x+1, x+2 都在 [a, b] 内，
    且这三个数两两互质（原题为典型 CF 题：找三个连续数，gcd(x,x+1,x+2)=1，
    条件可通过简单构造判断）。
    """
    if b - a + 1 < 3:
        return "-1"
    if a % 2 == 0:
        return f"{a} {a+1} {a+2}"
    if b - a + 1 > 3:
        return f"{a+1} {a+2} {a+3}"
    return "-1"


def main(n: int):
    """
    n 为规模参数，用于生成测试数据。
    这里生成 n 组 (a, b) 测试，并对每组执行一次 solve。
    生成规则：
    - a 在 [1, 10^6] 之间
    - 区间长度 len 在 [1, 10^5] 之间
    - b = a + len - 1
    """
    random.seed(0)

    max_a = 10**6
    max_len = 10**5

    results = []
    for _ in range(n):
        a = random.randint(1, max_a)
        length = random.randint(1, max_len)
        b = a + length - 1
        results.append(solve(a, b))

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    # 示例：运行 5 组随机测试
    main(5)