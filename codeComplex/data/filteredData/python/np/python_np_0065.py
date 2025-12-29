import math
import random


def c(k, n):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def main(n):
    # 根据规模 n 生成测试数据 sent 和 received
    # 这里约定：
    # - sent 为长度 n，由 '+' 和 '-' 随机组成
    # - received 为长度 n，由 '+', '-', '?' 随机组成
    sent = ''.join(random.choice(['+', '-']) for _ in range(n))
    received = ''.join(random.choice(['+', '-', '?']) for _ in range(n))

    difference = abs((sent.count('+') - sent.count('-')) -
                     (received.count('+') - received.count('-')))
    unrecognized = received.count('?')

    if difference > unrecognized:
        print(0)
        return

    k = (unrecognized - difference) // 2
    answer = c(k, unrecognized) * 0.5 ** unrecognized
    print(answer)


if __name__ == '__main__':
    # 示例：调用 main，n 为规模，可按需修改
    main(10)