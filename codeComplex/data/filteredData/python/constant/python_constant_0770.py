import random
import math

def main(n):
    # 根据规模 n 生成测试数据
    # 这里随机生成一个合法的 i in [0, n-1]，再反推出 k，保证原式存在整数解
    if n <= 0:
        return

    i_true = random.randint(0, n - 1)
    # 原式中：b = -(2n+3), c = n^2 + n - 2k，且 i 为一根：i^2 + b*i + c = 0
    # => c = -i^2 - b*i
    # 而 c = n^2 + n - 2k
    # => k = (n^2 + n - c) / 2
    b = -(2 * n + 3)
    c = -i_true * i_true - b * i_true
    k = (n * n + n - c) // 2  # 构造出的整数 k

    # 以下为原逻辑，仅使用 n, k（不再使用 input）
    b = -(2 * n + 3)
    c = n * n + n - 2 * k
    disc = b * b - 4 * c
    sqrt_disc = math.isqrt(disc)
    x = (-b - sqrt_disc) // 2
    y = (-b + sqrt_disc) // 2
    x, y = int(x), int(y)

    ans = None
    for i in [x - 1, x, x + 1, y - 1, y, y + 1]:
        if i * i + b * i + c == 0 and 0 <= i <= n - 1:
            ans = i
            break

    if ans is not None:
        print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)