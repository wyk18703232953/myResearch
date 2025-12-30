import math
import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 约定：a、b 的长度为 n
    # a 中只包含 '+' 和 '-'，b 中包含 '+', '-', '?' 三种
    # 保证 b 中至少有 1 个 '?'（前提 n > 0）
    if n <= 0:
        return

    # 生成 a：长度 n，随机 '+' / '-'
    a = ''.join(random.choice(['+', '-']) for _ in range(n))

    # 生成 b：先随机生成若干 '+', '-'，再保证至少一个 '?'
    b_list = [random.choice(['+', '-', '?']) for _ in range(n)]
    if '?' not in b_list:
        # 随机位置替换为 '?'
        pos = random.randrange(n)
        b_list[pos] = '?'
    b = ''.join(b_list)

    # 以下为原逻辑
    i = a.count('+')
    j = a.count('-')
    k = b.count('+')
    l = b.count('-')
    m = b.count('?')
    c1 = i - j
    c2 = k - l
    c = abs(c1 - c2)
    w = m - c
    x = w // 2
    y = w // 2 + c

    if c == 0 and m == 0:
        result = 1.0
    elif c > m:
        result = 0.0
    else:
        comb = math.factorial(m) // (math.factorial(x) * math.factorial(y))
        result = comb / (2 ** m)

    print(result)


if __name__ == "__main__":
    # 示例调用，规模可自行调整
    main(10)