import decimal
import random

def main(n):
    """
    n 作为规模参数，这里用来控制生成的 k 的大小范围：
    - k 在 [1, n] 内随机生成
    - n 本身也可按需调整（这里直接使用传入的 n）
    """
    # 生成测试数据
    # 为保证有意义，这里令 k 在 [1, max(1, n)] 内
    k = random.randint(1, max(1, n))

    # 原逻辑开始
    D = decimal.Decimal

    # 注意：原程序中的 n 和此处 main(n) 的参数同名，
    # 这里直接使用 main 的参数 n 作为原逻辑中的 n
    coef1 = (k * k - k - 2 * n) * 100 + 225
    if coef1 < 0:
        print('-1')
    else:
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