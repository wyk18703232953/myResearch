import math
import random

def main(n):
    # 生成规模为 n 的测试数据
    # sent 和 received 中只使用 '+', '-', '?' 三种字符
    # 这里设定：sent 和 received 的长度都为 n
    choices_sent = ['+', '-']
    choices_received = ['+', '-', '?']

    sent = ''.join(random.choice(choices_sent) for _ in range(n))
    received = ''.join(random.choice(choices_received) for _ in range(n))

    # 下面是原始逻辑
    sp = sent.count('+')
    sm = sent.count('-')
    rp = received.count('+')
    rm = received.count('-')
    quest = received.count('?')

    dist = sp - rp

    if dist < 0 or dist > quest:
        result = 0.0
    elif dist == 0 and quest == 0:
        result = 1.0
    else:
        total = 2 ** quest
        possible = math.factorial(quest) / math.factorial(dist) / math.factorial(quest - dist)
        result = possible / total

    # 按原程序行为，仅输出概率结果
    print(result)


if __name__ == "__main__":
    # 示例：可以在这里调用 main，n 为规模参数
    # 可根据需要修改 n
    main(10)