from math import factorial, pow

def main(n):
    # Deterministically generate send and received strings based on n.
    # Let length of both strings be n.
    # send pattern: "+-+-+..." (alternating starting with '+')
    # received pattern: positions divisible by 3 are '?',
    # others alternate "+-+-..." starting with '-'
    send = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    received_chars = []
    for i in range(n):
        if i % 3 == 0:
            received_chars.append('?')
        else:
            received_chars.append('+' if i % 2 == 1 else '-')
    received = ''.join(received_chars)

    pos = 0
    for p in send:
        pos = pos + 1 if p == '+' else pos - 1

    qcount = 0
    curr_pos = 0
    for p in received:
        if p == '+':
            curr_pos = curr_pos + 1
        elif p == '-':
            curr_pos = curr_pos - 1
        if p == '?':
            qcount += 1

    if qcount == 0:
        print("{:.12f}".format(1.0 if pos == curr_pos else 0.0))
    else:
        exp_val_q = abs(pos - curr_pos)
        if exp_val_q % 2 != qcount % 2 or qcount < exp_val_q:
            print("{:.12f}".format(0.0))
        else:
            neg = (qcount - exp_val_q) / 2
            posi = qcount - neg
            val = factorial(qcount) / (factorial(int(neg)) * factorial(int(posi)) * pow(2, qcount))
            print("{:.12f}".format(val))

if __name__ == "__main__":
    main(10)