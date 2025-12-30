from collections import Counter
import random
import string


def solve(n, ribbons):
    L = len(ribbons[0])
    a = [Counter(r).most_common(1)[0][1] for r in ribbons]

    r = sorted([(x, i) for i, x in enumerate(a)], reverse=True)

    if n == 1:
        c = Counter(a)
        if c[L - 1] == 1:
            for i in range(3):
                if a[i] == L - 1:
                    return i
        if c[L - 1] > 1:
            return 3
        if c[L] + c[L - 2] == 1:
            for i in range(3):
                if a[i] == L or a[i] == L - 2:
                    return i
        if c[L] + c[L - 2] > 1:
            return 3

    if r[1][0] == r[0][0]:
        return 3
    if r[1][0] + n >= L:
        return 3
    return r[0][1]


def main(n):
    # 生成规模为 n 的测试数据：
    # 使用长度为 max(n, 1) 的丝带，字符集为小写字母
    L = max(n, 1)
    alphabet = string.ascii_lowercase

    ribbons = [
        ''.join(random.choice(alphabet) for _ in range(L))
        for _ in range(3)
    ]

    cats = ('Kuro', 'Shiro', 'Katie', 'Draw')
    k = solve(n, ribbons)
    print(cats[k])


if __name__ == '__main__':
    # 示例：以 n = 3 运行
    main(3)