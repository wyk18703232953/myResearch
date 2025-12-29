import decimal
import random

def main(n: int):
    """
    n: 规模参数，用于生成测试数据。
       这里简单地令 k 在 [1, max(1, n)] 范围内随机生成。
    """
    # 生成测试数据
    k = random.randint(1, max(1, n))

    # 原始逻辑开始
    coef1 = (k * k - k - 2 * n) * 100 + 225
    if coef1 < 0:
        print(-1)
    else:
        D = decimal.Decimal
        coef11 = D(coef1)
        coef1 = coef11.sqrt()
        coef2 = k * 10 - 5
        coef = (coef2 - coef1) / 10
        if coef % 1 == 0:
            print(int(coef))
        else:
            print(int(coef) + 1)


if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)