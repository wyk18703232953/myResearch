import math

def main(n):
    # n controls the length of the strings
    length = max(1, n)

    # Deterministically construct s1: cycle through '+', '-' based on index
    s1 = ''.join('+' if i % 2 == 0 else '-' for i in range(length))

    # Deterministically construct s2:
    # positions divisible by 3 -> '?', mod 3 == 1 -> '+', mod 3 == 2 -> '-'
    s2 = ''.join(
        '?' if i % 3 == 0 else ('+' if i % 3 == 1 else '-')
        for i in range(length)
    )

    x = 0
    y = 0
    p = 0
    for i in range(len(s1)):
        if s1[i] == '+':
            x += 1
        elif s1[i] == '-':
            y += 1

        if s2[i] == '+':
            x -= 1
        elif s2[i] == '-':
            y -= 1
        else:
            p += 1

    if x < 0 or y < 0:
        print(float(0))
    else:
        q = math.factorial(x + y) / (math.factorial(x) * math.factorial(y))
        r = q / math.pow(2, p)
        print(r)


if __name__ == "__main__":
    main(10)