from math import factorial

def main(n):
    # Deterministically generate strings a and b based on n
    # a and b will have length n
    plus, minus, ques = '+', '-', '?'
    chars_a = []
    chars_b = []
    for i in range(n):
        # pattern for a: alternate '+', '-', with some bias
        if i % 3 == 0:
            chars_a.append(plus)
        elif i % 3 == 1:
            chars_a.append(minus)
        else:
            chars_a.append(plus)
        # pattern for b: periodic '+', '-', '?'
        r = i % 4
        if r == 0:
            chars_b.append(plus)
        elif r == 1:
            chars_b.append(minus)
        elif r == 2:
            chars_b.append(ques)
        else:
            chars_b.append(plus)
    a = ''.join(chars_a)
    b = ''.join(chars_b)

    ops1 = {plus: 0, minus: 0}
    ops2 = {plus: 0, minus: 0, ques: 0}
    for ai, bi in zip(a, b):
        ops1[ai] += 1
        ops2[bi] += 1
    final_pos = ops1[plus] - ops1[minus]
    initial_pos = ops2[plus] - ops2[minus]
    diff = final_pos - initial_pos
    abs_diff = abs(diff)
    if abs_diff > ops2[ques]:
        print(0.0)
    elif (ops2[ques] - abs_diff) % 2 != 0:
        print(0.0)
    else:
        total = 2 ** (ops2[ques])
        one_type = (ops2[ques] - abs_diff) // 2
        other_type = abs_diff + one_type
        numerator = factorial(ops2[ques]) / (factorial(one_type) * factorial(other_type))
        print(numerator / total)


if __name__ == "__main__":
    main(10)