import math

def compute_probability(sent, received):
    sp = sent.count('+')
    sm = sent.count('-')
    rp = received.count('+')
    rm = received.count('-')
    quest = received.count('?')
    dist = sp - rp

    if dist < 0 or dist > quest:
        return 0.0
    elif dist == 0 and quest == 0:
        return 1.0
    else:
        total = 2 ** quest
        possible = math.factorial(quest) / math.factorial(dist) / math.factorial(quest - dist)
        return possible / total

def main(n):
    if n < 1:
        n = 1
    # sent length and received length both grow with n
    sent_len = n
    recv_len = n

    # deterministic construction:
    # sent: first half '+', second half '-'
    half = sent_len // 2
    sent = ''.join('+' if i < half else '-' for i in range(sent_len))

    # received: cycle through '+', '-', '?'
    pattern = ['+', '-', '?']
    received = ''.join(pattern[i % 3] for i in range(recv_len))

    result = compute_probability(sent, received)
    print(result)

if __name__ == "__main__":
    main(10)