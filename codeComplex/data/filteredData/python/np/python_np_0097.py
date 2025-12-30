import math
import random

def main(n):
    # 生成测试数据：
    # 根据 n 生成长度为 n 的字符串 a、b，字符来自 '+', '-', '?'
    # 保证 b 中含有若干 '?' 以体现随机性的计算场景
    chars = ['+', '-', '?']
    a = ''.join(random.choice(chars) for _ in range(n))
    b = ''.join(random.choice(chars) for _ in range(n))

    x = a.count('+') - b.count('+')
    y = a.count('-') - b.count('-')
    c = a.count('+') - a.count('-')
    d = b.count('+') - b.count('-')
    e = c - d
    f = b.count('?')

    if x == 0 and y == 0:
        result = 1
    elif f == 0 and (x != 0 or y != 0):
        result = 0
    elif x != 0 and y == 0:
        result = 1 / 2 ** f
    elif y != 0 and x == 0:
        result = 1 / 2 ** f
    elif abs(e) > f:
        result = 0
    else:
        result = math.factorial(f) / (math.factorial(y) * math.factorial(x) * 2 ** f)

    print(result)
    return result

if __name__ == "__main__":
    # 示例调用：n 为规模参数
    main(10)