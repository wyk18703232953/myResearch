import math
import random

def cnt_digit_order(X: int) -> int:
    res = 0
    if X == 0:
        return 0
    for i in range(1, X + 1):
        res += i * (9 * pow(10, i - 1))
    return res


def solve_for_k(k: int) -> str:
    L = -1
    leftcnt = 0
    for length in range(1, 100):
        if cnt_digit_order(length - 1) < k <= cnt_digit_order(length):
            L = length
            leftcnt = k - cnt_digit_order(length - 1)
            break

    M = str(math.ceil(leftcnt / L) + (10 ** (L - 1) - 1))
    leftcnt -= 1
    leftcnt %= L
    return M[leftcnt]


def main(n: int):
    # 根据规模 n 生成测试数据：生成一个正整数 k
    # 令 k 大致在 [1, 10^n] 的范围内（上界做个限制防止过大）
    max_k = 10 ** min(n, 12)
    k = random.randint(1, max_k)

    # 核心逻辑
    ans = solve_for_k(k)
    print(ans)


if __name__ == "__main__":
    # 示例：可以修改这里的 n 进行规模测试
    main(5)