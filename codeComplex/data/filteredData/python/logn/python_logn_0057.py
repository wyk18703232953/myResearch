from math import log
import random

def main(n: int):
    # 1. 根据规模 n 生成测试数据
    # 这里简单设定：
    #   1 <= l <= r <= 2^n - 1
    #   随机生成 l, r
    if n <= 0:
        return
    max_val = (1 << n) - 1
    l = random.randint(1, max_val)
    r = random.randint(l, max_val)

    # 2. 原始逻辑（去掉 input()），计算结果
    # 为避免 log(0,2) 出错，处理边界
    if l == 0 and r == 0:
        print(0)
        return
    if l == 0:
        msb = int(log(r, 2))
    elif r == 0:
        msb = int(log(l, 2))
    else:
        msb = int(max(log(l, 2), log(r, 2)))

    i = msb
    while ((1 << i) & l) == ((1 << i) & r):
        i -= 1
        if i == -1:
            break
    i += 1
    print((1 << i) - 1)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)