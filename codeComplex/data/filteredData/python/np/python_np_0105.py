import math

def find_nCr(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

def build_inputs(n):
    length = max(1, n)
    # sent: first half '+', second half '-'
    sent = "".join("+" if i < length // 2 else "-" for i in range(length))
    # received: pattern with some '?'
    received_chars = []
    for i in range(length):
        if i % 3 == 0:
            received_chars.append("?")
        elif i % 3 == 1:
            received_chars.append("+")
        else:
            received_chars.append("-")
    received = "".join(received_chars)
    return sent, received

def main(n):
    sent, received = build_inputs(n)

    final_pos = 0
    current_pos = 0
    uncertain = 0

    for s in sent:
        if s == "+":
            final_pos += 1
        else:
            final_pos -= 1

    for s in received:
        if s == "+":
            current_pos += 1
        elif s == "-":
            current_pos -= 1
        else:
            uncertain += 1

    if uncertain == 0:
        if final_pos == current_pos:
            print(1)
        else:
            print(0)
    else:
        positions = list(range(current_pos - uncertain, current_pos + uncertain + 2, 2))
        try:
            pos_index = positions.index(final_pos)
            a = find_nCr(uncertain, pos_index)
            b = math.pow(2, uncertain)
            print(a / b)
        except ValueError:
            print(0)

if __name__ == "__main__":
    main(10)