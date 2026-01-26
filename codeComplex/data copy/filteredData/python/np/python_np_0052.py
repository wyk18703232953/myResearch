import math
from math import factorial

def combination(n, r):
    return float(factorial(n)) / float(factorial(r)) / float(factorial(n - r))

def original_logic(a, b):
    ap = a.count('+')
    am = a.count('-')
    bp = b.count('+')
    bm = b.count('-')
    n = b.count('?')
    x = float(ap - bp)
    y = float(am - bm)
    if x < 0 or y < 0 or x + y != n:
        return 0.0
    else:
        return combination(n, x) / (1 << n)

def generate_strings(n):
    # Deterministically generate strings a and b of length n
    # pattern: positions divisible by 3 -> '+', divisible by 5 -> '-', else '+'
    a_chars = []
    b_chars = []
    for i in range(n):
        if i % 3 == 0:
            a_chars.append('+')
        elif i % 5 == 0:
            a_chars.append('-')
        else:
            a_chars.append('+')
        if i % 4 == 0:
            b_chars.append('+')
        elif i % 2 == 0:
            b_chars.append('-')
        else:
            b_chars.append('?')
    return ''.join(a_chars), ''.join(b_chars)

def main(n):
    a, b = generate_strings(n)
    result = original_logic(a, b)
    print(result)

if __name__ == "__main__":
    main(10)