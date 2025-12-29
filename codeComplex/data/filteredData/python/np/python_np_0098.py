import math
import random

def main(n: int):
    # 1. 随机生成目标串 s：长度为 n，由 '+' 和 '-' 组成
    s = ''.join(random.choice('+-') for _ in range(n))
    # 2. 随机生成观测串 s2：长度为 n，由 '+', '-', '?' 组成
    s2 = ''.join(random.choice('+-?') for _ in range(n))

    p = s.count("+")
    m = s.count("-")
    q = s2.count("+")
    w = s2.count("-")
    pr, mr = p - q, m - w

    if pr < 0 or mr < 0:
        ans = 0.0
    else:
        temp = pr + mr
        if temp == 0:
            ans = 1.0
        else:
            total = 2 ** temp
            res = math.factorial(temp) / (math.factorial(pr) * math.factorial(mr))
            ans = res / total

    print(f"{ans:.12f}")
    # 如需查看生成的数据，可取消下两行注释：
    # print("s =", s)
    # print("s2 =", s2)


if __name__ == "__main__":
    # 示例：规模 n=10
    main(10)