import math
from math import factorial

def combination(n, r):
    return float(factorial(n)) / float(factorial(r)) / float(factorial(n - r))

def core_logic(a, b):
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

def generate_inputs(n):
    # Generate deterministic strings a and b based on n
    if n <= 0:
        n = 1
    # a: first half '+', second half '-'
    half = n // 2
    a = '+' * half + '-' * (n - half)
    # b: pattern of '+', '-', '?' repeating
    pattern = ['+', '-', '?']
    b = ''.join(pattern[i % 3] for i in range(n))
    return a, b

def main(n):
    a, b = generate_inputs(n)
    result = core_logic(a, b)
    print(result)

if __name__ == "__main__":
    main(10)