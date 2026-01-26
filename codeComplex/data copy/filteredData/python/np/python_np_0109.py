from math import factorial

def generate_inputs(n):
    # Generate s1 and s2 of length n using deterministic patterns
    # s1 pattern: first n//3 are '+', next n//3 are '-', rest alternate '+', '-'
    s1 = []
    for i in range(n):
        if i < n // 3:
            s1.append('+')
        elif i < 2 * n // 3:
            s1.append('-')
        else:
            s1.append('+' if (i - 2 * n // 3) % 2 == 0 else '-')
    s1 = ''.join(s1)

    # s2 pattern:
    # positions divisible by 3: '?'
    # positions %3 == 1: '+'
    # positions %3 == 2: '-'
    s2 = []
    for i in range(n):
        if i % 3 == 0:
            s2.append('?')
        elif i % 3 == 1:
            s2.append('+')
        else:
            s2.append('-')
    s2 = ''.join(s2)

    return s1, s2

def core_logic(s1, s2):
    cnt_plus_1, cnt_plus_2 = 0, 0
    cnt_minus_1, cnt_minus_2 = 0, 0
    cnt_question = 0

    for i in range(len(s1)):
        if s1[i] == "+":
            cnt_plus_1 += 1
        if s1[i] == "-":
            cnt_minus_1 += 1

        if s2[i] == "+":
            cnt_plus_2 += 1
        if s2[i] == "-":
            cnt_minus_2 += 1

        if s2[i] == "?":
            cnt_question += 1

    if cnt_question == 0:
        if cnt_plus_1 == cnt_plus_2:
            return float("{:.9f}".format(1.0))
        else:
            return float("{:.9f}".format(0.0))
    elif cnt_plus_2 + cnt_question < cnt_plus_1 or cnt_plus_2 > cnt_plus_1:
        return float("{:.9f}".format(0.0))
    else:
        dP = cnt_plus_1 - cnt_plus_2
        dM = cnt_question - dP

        if dM == 0 or dP == 0:
            return float("{:0.9f}".format(1 / (2 ** cnt_question)))
        else:
            CP = factorial(cnt_question) / (factorial(dP) * factorial(cnt_question - dP))
            return CP * (0.5 ** dP) * (1 - 0.5) ** (cnt_question - dP)

def main(n):
    s1, s2 = generate_inputs(n)
    result = core_logic(s1, s2)
    print("{:.9f}".format(result))

if __name__ == "__main__":
    main(10)