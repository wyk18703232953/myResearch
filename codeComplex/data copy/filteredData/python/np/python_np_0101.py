import math

def main(n):
    # n controls the length of s1 and s2
    # Generate s1: first half '+', second half '-'
    half = n // 2
    s1 = '+' * half + '-' * (n - half)

    # Generate s2 based on s1 deterministically:
    # positions divisible by 3 -> '?'
    # even index (0-based) and not divisible by 3 -> same as s1
    # odd index and not divisible by 3 -> opposite of s1
    s2_chars = []
    for i, ch in enumerate(s1):
        if i % 3 == 0:
            s2_chars.append('?')
        else:
            if i % 2 == 0:
                s2_chars.append(ch)
            else:
                s2_chars.append('+' if ch == '-' else '-')
    s2 = ''.join(s2_chars)

    d1 = 0
    d2 = 0
    q = 0
    answer = 0.0

    for i in s1:
        if i == '+':
            d1 += 1
        else:
            d1 -= 1
    for i in s2:
        if i == '+':
            d2 += 1
        elif i == '?':
            q += 1
        else:
            d2 -= 1

    if q >= abs(d2 - d1):
        y = (q - abs(d1 - d2)) / 2
        if y % 1 == 0:
            y_int = int(y)
            answer = (
                math.factorial(q)
                / math.factorial(q - y_int)
                / math.factorial(y_int)
                / (2 ** q)
            )

    print('%.9f' % answer)


if __name__ == "__main__":
    main(10)