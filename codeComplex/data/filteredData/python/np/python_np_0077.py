import math
import random

def main(n):
    # 生成测试数据：
    # s1：长度为 n，仅包含'+'或'-'
    # s2：长度为 n，包含'+', '-', '?'，其中'?'表示原程序中的未知位置
    choices_s1 = ['+', '-']
    choices_s2 = ['+', '-', '?']

    s1 = ''.join(random.choice(choices_s1) for _ in range(n))
    s2 = ''.join(random.choice(choices_s2) for _ in range(n))

    x = 0
    y = 0
    p = 0
    for i in range(len(s1)):
        if s1[i] == '+':
            x += 1
        elif s1[i] == '-':
            y += 1

        if s2[i] == '+':
            x -= 1
        elif s2[i] == '-':
            y -= 1
        else:
            p += 1

    if x < 0 or y < 0:
        print(float(0))
    else:
        q = math.factorial(x + y) / (math.factorial(x) * math.factorial(y))
        r = q / math.pow(2, p)
        print(r)

if __name__ == "__main__":
    # 示例：规模 n=10
    main(10)