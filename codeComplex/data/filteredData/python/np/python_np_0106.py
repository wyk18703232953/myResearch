import math

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
    total_len = sum(actual_sequence)
    actual_ans = actual_sequence[0] - actual_sequence[1]
    ans_received = sequence_received[0] - sequence_received[1]
    difference = actual_ans - ans_received
    no_of_blanks = sequence_received[2]
    if no_of_blanks == 0:
        if actual_ans != ans_received:
            return 0
        return 1
    if abs(difference) > no_of_blanks:
        return 0
    ans_set = [0, 0]
    if difference > 0:
        ans_set[0] += difference
    elif difference < 0:
        ans_set[1] += abs(difference)
    blanks_left = no_of_blanks - abs(difference)
    ans_set[0] = ans_set[0] + blanks_left // 2
    ans_set[1] = ans_set[1] + blanks_left // 2
    x = (math.factorial(no_of_blanks) // (math.factorial(ans_set[0]) * math.factorial(ans_set[1]))) / math.pow(2, no_of_blanks)
    return x

def generate_sequences(n):
    # n controls the length of the sequences
    length = max(1, n)
    # drazil_send: deterministic pattern of '+' and '-'
    drazil = []
    for i in range(length):
        if i % 2 == 0:
            drazil.append('+')
        else:
            drazil.append('-')
    drazil_send = ''.join(drazil)
    # dreamoon_received: same length, with some positions turned into '?'
    dreamoon = []
    for i in range(length):
        if i % 3 == 0:
            dreamoon.append('?')
        else:
            dreamoon.append(drazil[i])
    dreamoon_received = ''.join(dreamoon)
    return drazil_send, dreamoon_received

def main(n):
    drazil_send, dreamoon_received = generate_sequences(n)
    result = probability(drazil_send, dreamoon_received)
    print("{:.12f}".format(result))

if __name__ == "__main__":
    main(10)