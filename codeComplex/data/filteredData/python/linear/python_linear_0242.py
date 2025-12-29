from collections import Counter
import random
import string


def main(n: int):
    # 根据 n 生成测试数据：生成三条长度为 n 的随机字符串
    # 字符集选择大写字母，可按需要修改
    def gen_str(length):
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

    a = gen_str(n)
    b = gen_str(n)
    c = gen_str(n)

    fa = Counter(a)
    fb = Counter(b)
    fc = Counter(c)

    la = min(fa.most_common(1)[0][1] + n, len(a))
    lb = min(fb.most_common(1)[0][1] + n, len(b))
    lc = min(fc.most_common(1)[0][1] + n, len(c))

    if fa.most_common(1)[0][1] == len(a) and n == 1:
        la = len(a) - 1

    if fb.most_common(1)[0][1] == len(b) and n == 1:
        lb = len(b) - 1

    if fc.most_common(1)[0][1] == len(c) and n == 1:
        lc = len(c) - 1

    if la > max(lb, lc):
        print("Kuro")
    elif lb > max(la, lc):
        print("Shiro")
    elif lc > max(la, lb):
        print("Katie")
    else:
        print("Draw")


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改
    main(5)