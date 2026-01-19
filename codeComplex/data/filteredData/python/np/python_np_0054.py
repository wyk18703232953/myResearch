import math

def main(n):
    # n controls the length of s1 and s2
    length = max(1, n)

    # Deterministically generate s1 and s2 based on length
    # Pattern cycles through '+', '-', '?'
    symbols = ['+', '-', '?']
    s1 = [symbols[i % 3] for i in range(length)]
    s2 = [symbols[(i + 1) % 3] for i in range(length)]

    p1 = m1 = p2 = m2 = c = 0
    for i in range(len(s1)):
        if s1[i] == '+':
            p1 += 1
        if s1[i] == '-':
            m1 += 1
        if s2[i] == '+':
            p2 += 1
        if s2[i] == '-':
            m2 += 1
        if s2[i] == '?':
            c += 1
    p = abs(p1 - p2)
    m = abs(m1 - m2)
    if (p + m) == c:
        result = math.factorial(c) / (math.factorial(p) * math.factorial(m) * pow(2, c))
    else:
        result = 0 / 1
    print(result)


if __name__ == "__main__":
    main(10)