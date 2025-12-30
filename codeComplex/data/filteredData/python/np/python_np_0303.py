import random

MOD = 998244353

def solve(n, k):
    if k > 2 * n:
        return 0
    if k == 2 * n or k == 1:
        return 2

    iguales = [0] * (k + 1)
    diferentes = [0] * (k + 1)

    iguales[1] = 2
    diferentes[2] = 2

    for _ in range(1, n):
        auxigual = [0] * (k + 1)
        auxdiff = [0] * (k + 1)

        for j in range(1, k + 1):
            auxigual[j] = (iguales[j] + iguales[j - 1] + 2 * diferentes[j]) % MOD

        for j in range(2, k + 1):
            auxdiff[j] = (diferentes[j] + diferentes[j - 2] + 2 * iguales[j - 1]) % MOD

        iguales = auxigual
        diferentes = auxdiff

    return (iguales[-1] + diferentes[-1]) % MOD


def main(n):
    # 根据规模 n 生成测试数据：k 在 [1, 2n] 范围内随机选择（保证有意义）
    if n <= 0:
        return None  # 或者根据需要调整
    k = random.randint(1, 2 * n)
    return solve(n, k)


if __name__ == "__main__":
    # 示例：指定一个 n 来运行
    n_example = 10
    print(main(n_example))