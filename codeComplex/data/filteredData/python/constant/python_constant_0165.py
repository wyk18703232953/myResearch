import random
import math

def main(n: int):
    # 1. 生成测试数据 [l, r]，保证区间长度为 j = n（n >= 1）
    #    随机选择 l，r = l + n - 1
    if n < 1:
        raise ValueError("n must be >= 1")
    l = random.randint(1, 10**6)
    r = l + n - 1
    j = r - l + 1

    # 2. 原逻辑：在 [l, r] 中找三个两两互质的数（原题的“coprime”逻辑）
    if j == 3:
        if l % 2 == 0:
            print(l, l + 1, l + 2)
        else:
            print(-1)
    elif j > 3:
        if l % 2 == 0:
            print(l, l + 1, l + 2)
        else:
            print(l + 1, l + 2, l + 3)
    else:
        print(-1)

if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)