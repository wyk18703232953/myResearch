from math import factorial
import random

def main(n: int):
    # 生成测试数据 s1, s2，长度设为 n
    # s1 只包含 '+' 和 '-'
    # s2 包含 '+', '-', '?'，使得 '?' 的数量也受规模 n 控制

    # 随机生成 s1
    s1 = ''.join(random.choice(['+', '-']) for _ in range(n))

    # 随机生成 s2，其中部分字符为 '?'
    # 控制一下 '?' 的期望数量，约为 n/3
    choices = ['+', '-', '?']
    weights = [3, 3, 2]  # 可调权重
    s2_list = []
    for _ in range(n):
        r = random.randint(1, sum(weights))
        cum = 0
        for ch, w in zip(choices, weights):
            cum += w
            if r <= cum:
                s2_list.append(ch)
                break
    s2 = ''.join(s2_list)

    # 原逻辑开始
    n_q = 0
    x1 = 0
    for ch in s1:
        if ch == '+':
            x1 += 1
        else:
            x1 -= 1

    x2 = 0
    for ch in s2:
        if ch == '+':
            x2 += 1
        elif ch == '?':
            n_q += 1
        else:
            x2 -= 1

    x = abs(x1 - x2)
    if x > n_q:
        ans = 0.0
    elif x == n_q:
        ans = 1 / (2 ** n_q)
    else:
        if (n_q - x) % 2 == 1:
            ans = 0.0
        else:
            k = (n_q - x) // 2
            comb = factorial(n_q) // (factorial(k) * factorial(n_q - k))
            ans = comb / (2 ** n_q)

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)