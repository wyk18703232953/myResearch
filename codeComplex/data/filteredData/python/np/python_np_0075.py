from math import factorial, pow
import random


def solve(send: str, received: str) -> float:
    pos = 0
    for p in send:
        pos = pos + 1 if p == '+' else pos - 1

    qcount = 0
    curr_pos = 0
    for p in received:
        if p == '+':
            curr_pos += 1
        elif p == '-':
            curr_pos -= 1
        if p == '?':
            qcount += 1

    if qcount == 0:
        return 1.0 if pos == curr_pos else 0.0
    else:
        exp_val_q = abs(pos - curr_pos)
        if exp_val_q % 2 != qcount % 2 or qcount < exp_val_q:
            return 0.0
        else:
            neg = (qcount - exp_val_q) / 2
            posi = qcount - neg
            val = factorial(qcount) / (factorial(int(neg)) *
                                       factorial(int(posi)) *
                                       pow(2, qcount))
            return val


def generate_test_data(n: int):
    # 生成长度为 n 的 send 序列（只含 '+' 或 '-'）
    send = ''.join(random.choice('+-') for _ in range(n))

    # 生成长度为 n 的 received 序列（含 '+', '-', '?'）
    received_chars = ['+', '-', '?']
    received = ''.join(random.choice(received_chars) for _ in range(n))

    return send, received


def main(n: int):
    send, received = generate_test_data(n)
    ans = solve(send, received)
    print("{:.12f}".format(ans))


if __name__ == "__main__":
    # 示例：n = 5，可根据需要修改或在外部调用 main(n)
    main(5)