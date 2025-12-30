from math import inf
import random

def solve(a0: str, a1: str) -> int:
    a = [list(a0.strip()), list(a1.strip())]
    an = [-inf, -inf, -inf]

    if a[0][0] == a[1][0] == '0':
        an[0] = 0
    elif a[0][0] != a[1][0]:
        an[1] = 0

    x = 0
    for i in range(1, len(a[0])):
        if an[0] == 0:
            if a[0][i] == a[1][i] == '0':
                x += 1
                an = [-inf, 0, -inf]
            elif a[0][i] != a[1][i]:
                x += 1
                an = [-inf] * 3
            else:
                an = [-inf, -inf, -inf]
        elif an[1] == 0:
            if a[0][i] == a[1][i] == '0':
                x += 1
                an = [-inf, -inf, -inf]
            elif a[0][i] != a[1][i]:
                pass
            else:
                an = [-inf, -inf, -inf]
        else:
            if a[0][i] == a[1][i] == '0':
                an = [0, -inf, -inf]
            elif a[0][i] != a[1][i]:
                an = [-inf, 0, -inf]
            else:
                an = [-inf, -inf, -inf]
    return x


def main(n: int):
    # 生成长度为 n 的二进制字符串
    a0 = ''.join(random.choice('01') for _ in range(n))
    a1 = ''.join(random.choice('01') for _ in range(n))
    # 调用原逻辑
    result = solve(a0, a1)
    print(result)


if __name__ == '__main__':
    # 示例：规模为 10
    main(10)