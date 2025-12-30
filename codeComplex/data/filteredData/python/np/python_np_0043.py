from math import factorial
import random

def main(n):
    # 生成测试数据：长度为 n 的 s 和 s1
    # s 中不含 '?'，只含 '+' 和 '-'
    # s1 中含 '+', '-', '?' 的混合
    s = ''.join(random.choice('+-') for _ in range(n))
    s1 = ''.join(random.choice('+-?') for _ in range(n))

    plus = s.count('+') - s1.count('+')
    minus = s.count('-') - s1.count('-')
    q = s1.count('?')

    if plus < 0 or minus < 0:
        ans = 0.0
    else:
        # C(q, plus) * (0.5 ** q)
        if plus > q:
            ans = 0.0
        else:
            ans = factorial(q) / (factorial(q - plus) * factorial(plus)) * (0.5 ** q)

    print(ans)


if __name__ == "__main__":
    # 示例调用：n 为规模
    main(10)