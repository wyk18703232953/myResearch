import math as m

def main(n):
    # Generate deterministic inputs a and b based on n
    # a and b are strings containing '+', '-' and '?' (for unknown in original problem)
    length = max(1, n)
    a = ''.join('+' if i % 2 == 0 else '-' for i in range(length))
    b = []
    for i in range(length):
        if i % 3 == 0:
            b.append('+')
        elif i % 3 == 1:
            b.append('-')
        else:
            b.append('?')
    b = ''.join(b)

    total_sum = 0
    req_pos = 0
    unreco = 0

    for i in a:
        if i == '+':
            total_sum += 1
            req_pos += 1
        elif i == '-':
            total_sum -= 1

    for i in b:
        if i == '+':
            total_sum -= 1
            req_pos -= 1
        elif i == '-':
            total_sum += 1
        else:
            unreco += 1

    if total_sum == 0 and unreco == 0:
        print(1.000000000)
    elif abs(total_sum) > unreco or req_pos < 0:
        print(0.000000000)
    else:
        ans = m.factorial(unreco) / (m.factorial(req_pos) * m.factorial(unreco - req_pos) * (2 ** unreco))
        print(ans)


if __name__ == "__main__":
    main(10)