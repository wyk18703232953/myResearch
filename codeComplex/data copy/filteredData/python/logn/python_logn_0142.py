import math
from decimal import Decimal

def sum2(s, e):
    return sum1(e) - sum1(s - Decimal(1)) - (e - s)

def sum1(i):
    return i * (i + 1) / 2

def main(n):
    # 生成确定性输入：
    # 对应原来的一行 "n k"
    # 映射规则：
    #   N = n + 1
    #   K = max(1, n // 2)
    N = Decimal(n + 1)
    K = Decimal(max(1, n // 2))

    if N == 1:
        # print(0)
        pass
    elif K > N:
        # print(1)
        pass
    elif sum2(Decimal(2), K) < N:
        # print(-1)
        pass

    else:
        c = 2 * N + K - K * K
        discriminant = (9 - 4 * c).sqrt()
        res1 = math.floor((3 + discriminant) / 2)
        res2 = math.floor((3 - discriminant) / 2)
        res1 = max(res1, res2)
        # print(int(K - res1 + 1))
        pass
if __name__ == "__main__":
    main(10)