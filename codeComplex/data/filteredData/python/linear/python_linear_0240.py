from collections import Counter
import random
import string


def f(x: str) -> int:
    return max(Counter(x).values())


def v(x: int, l: int) -> int:
    if x == l:
        return x - 1
    else:
        return x + 1


def main(n: int):
    # 1. 根据 n 生成测试数据
    # 设三个字符串长度均为 n，字符从小写字母中随机生成
    l = n
    letters = string.ascii_lowercase

    z = ''.join(random.choice(letters) for _ in range(l))
    s2 = ''.join(random.choice(letters) for _ in range(l))
    s3 = ''.join(random.choice(letters) for _ in range(l))

    # 2. 按原逻辑计算
    a = f(z)
    b = f(s2)
    c = f(s3)

    if n == 1:
        a, b, c = v(a, l), v(b, l), v(c, l)
        if a > b and a > c:
            print("Kuro")
        elif b > a and b > c:
            print("Shiro")
        elif c > a and c > b:
            print("Katie")
        else:
            print("Draw")
    elif (l - a <= n) + (l - b <= n) + (l - c <= n) >= 2:
        print("Draw")
    elif a > b and a > c:
        print("Kuro")
    elif b > a and b > c:
        print("Shiro")
    elif c > a and c > b:
        print("Katie")
    else:
        print("Draw")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)