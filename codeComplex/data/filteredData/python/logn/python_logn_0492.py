import math
import random

def main(n: int):
    # 根据 n 生成一个“目标位置” t，范围为 [1, n]
    # 原逻辑是：给定 t，求第 t 个数字（从 1 开始计数）在无限串 "123456789101112..." 中对应的数字字符
    if n <= 0:
        return
    t = random.randint(1, n)

    a = [9]
    for i in range(2, 20):
        a.append(10 ** i - 10 ** (i - 1))  # i 位数一共有多少个

    b = [0]
    for i in range(1, 20):
        b.append(b[-1] + i * a[i - 1])     # i 位数贡献的总位数前缀和

    # 找到 t 所在的位数区间
    for i in range(20):
        if t <= b[i]:
            break

    p = b[i - 1]  # 之前位数总共占的长度
    k = t - p     # 在当前位数段中的第 k 位（从 1 开始）

    ans = 10 ** (i - 1) - 1 + math.ceil(k / i)  # 对应的实际数字

    s = '0' + str(ans)
    if k % i == 0:
        print(s[i])
    else:
        print(s[k % i])


if __name__ == "__main__":
    # 示例调用：规模 n 可以按需调整
    main(10**6)