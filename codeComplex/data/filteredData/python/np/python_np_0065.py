import math


def c(k, n):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def main(n):
    # 规模含义：
    # sent / received 的长度均为 n
    # 构造方式完全确定：
    # sent: 前 n//2 个为 '+', 其余为 '-'
    # received: 交替 '+', '-', 其余为 '?'
    if n <= 0:
        return

    half = n // 2
    sent = '+' * half + '-' * (n - half)

    prefix_len = n // 3
    alt = ['+', '-']
    received_list = []
    for i in range(prefix_len):
        received_list.append(alt[i % 2])
    received_list.extend('?' * (n - prefix_len))
    received = ''.join(received_list)

    difference = abs((sent.count('+') - sent.count('-')) - (received.count('+') - received.count('-')))
    unrecognized = received.count('?')
    if difference > unrecognized:
        print(0)
        return
    k = (unrecognized - difference) // 2
    answer = c(k, unrecognized) * 0.5 ** unrecognized
    print(answer)


if __name__ == "__main__":
    main(10)