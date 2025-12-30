import math
import random

def cm(n, r):
    i = n - r
    return math.factorial(n) // (math.factorial(i) * math.factorial(r))

def main(n):
    # 生成测试数据 s1, s2，长度规模由 n 决定
    # 这里简单设定：总长度为 n，s1 不含 '?'，s2 含若干 '?'
    # 你可根据需要修改生成策略
    choices = ['+', '-']
    choices_with_q = ['+', '-', '?']

    # 让 s1 和 s2 长度都为 n
    s1 = ''.join(random.choice(choices) for _ in range(n))
    s2 = ''.join(random.choice(choices_with_q) for _ in range(n))

    d1 = {'+': 0, '-': 0}
    d2 = {'+': 0, '-': 0, '?': 0}

    for c in s1:
        d1[c] += 1
    for c in s2:
        d2[c] += 1

    np_diff = d1['+'] - d2['+']
    nn_diff = d1['-'] - d2['-']

    if np_diff < 0 or nn_diff < 0:
        ans = 0
    else:
        qn = d2['?']
        r = min(np_diff, nn_diff)
        ans = cm(qn, r)
        ans = round(float(ans) / float(math.pow(2, qn)), 9)

    print(ans)

if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)