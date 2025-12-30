import math
import random

def sequence_split_up(sequence):
    ans = [0, 0, 0]
    for i in sequence:
        if i == '+':
            ans[0] += 1
        elif i == '-':
            ans[1] += 1
        elif i == '?':
            ans[2] += 1
    return ans

def probability(drazil_send, dreamoon_received):
    actual_sequence = sequence_split_up(drazil_send)
    sequence_received = sequence_split_up(dreamoon_received)
    actual_ans = actual_sequence[0] - actual_sequence[1]
    ans_received = sequence_received[0] - sequence_received[1]
    difference = actual_ans - ans_received
    no_of_blanks = sequence_received[2]

    if no_of_blanks == 0:
        if actual_ans != ans_received:
            return 0.0
        return 1.0

    if abs(difference) > no_of_blanks:
        return 0.0

    ans_set = [0, 0]
    if difference > 0:
        ans_set[0] += difference
    elif difference < 0:
        ans_set[1] += abs(difference)

    blanks_left = no_of_blanks - abs(difference)
    ans_set[0] = ans_set[0] + blanks_left // 2
    ans_set[1] = ans_set[1] + blanks_left // 2

    x = (math.factorial(no_of_blanks) //
         (math.factorial(ans_set[0]) * math.factorial(ans_set[1]))) / math.pow(2, no_of_blanks)
    return x

def generate_test_data(n):
    # 生成长度为 n 的 drazil_send，仅包含 '+' 和 '-'
    drazil_send = ''.join(random.choice(['+', '-']) for _ in range(n))

    # 从 drazil_send 生成 dreamoon_received：
    # 对每个位置，以一定概率变为 '?'，否则保持原符号
    dreamoon_received = []
    for ch in drazil_send:
        # 约 1/3 概率变为 '?'
        if random.random() < 1.0 / 3.0:
            dreamoon_received.append('?')
        else:
            dreamoon_received.append(ch)
    dreamoon_received = ''.join(dreamoon_received)
    return drazil_send, dreamoon_received

def main(n):
    drazil_send, dreamoon_received = generate_test_data(n)
    ans = probability(drazil_send, dreamoon_received)
    print(f"drazil_send:      {drazil_send}")
    print(f"dreamoon_received:{dreamoon_received}")
    print(f"{ans:.12f}")

if __name__ == "__main__":
    # 示例：可在此修改规模 n
    main(10)