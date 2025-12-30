import itertools
import random

def main(n):
    # 1. 生成规模为 n 的测试数据
    # s1, s2 长度都为 n，字符来自 '+', '-', '?'
    chars = ['+', '-', '?']
    s1 = ''.join(random.choice(chars) for _ in range(n))
    s2 = ''.join(random.choice(chars) for _ in range(n))

    # 2. 逻辑部分（与原程序一致）
    kol1 = {'+': 0, '-': 0, '?': 0}
    kol2 = {'+': 0, '-': 0, '?': 0}

    for ch in s1:
        kol1[ch] += 1

    for ch in s2:
        kol2[ch] += 1

    if kol1['+'] == kol2['+'] and kol1['-'] == kol2['-']:
        print('1.0')
        return

    mod1 = kol1['+'] - kol1['-']
    mod2 = kol2['+'] - kol2['-']
    mod3 = abs(mod2 - mod1)

    if mod3 > kol2['?']:
        print(0.0)
        return

    list_comb = [1, -1]
    sum_pos = 0
    col = 0

    for comb in itertools.product(list_comb, repeat=kol2['?']):
        if sum(comb) == mod3:
            sum_pos += 1
        col += 1

    print(sum_pos / col)


if __name__ == "__main__":
    # 示例：n = 5
    main(5)