import math
import random

def main(n):
    # 生成测试数据，这里将 n 作为 k 的上界随机生成一个 1..n 的整数
    # 如需固定数据，可将下面一行改为：k = n
    k = random.randint(1, n)

    flag = True
    i = 0
    value = 0

    if k <= 9:
        print(k)
    else:
        while flag:
            a = 9 * pow(10, i) * (i + 1)
            if k >= a:
                k -= a
                value += 9 * pow(10, i)
                i += 1
            else:
                n_val = int(math.ceil(k / (i + 1)))
                value += n_val
                index = k % (i + 1) - 1
                print(str(value)[index])
                flag = False