import math

def compute_probability(a, b):
    x = a.count('+') - b.count('+')
    y = a.count('-') - b.count('-')
    c = a.count('+') - a.count('-')
    d = b.count('+') - b.count('-')
    e = c - d
    f = b.count('?')
    if x == 0 and y == 0:
        return 1
    elif f == 0 and (x != 0 or y != 0):
        return 0
    elif x != 0 and y == 0:
        return 1 / 2 ** f
    elif y != 0 and x == 0:
        return 1 / 2 ** f
    elif abs(e) > f:
        return 0
    else:
        return math.factorial(f) / (math.factorial(y) * math.factorial(x) * 2 ** f)

def main(n):
    # Input structure: two strings a, b composed of '+', '-', '?'
    # n controls the length of these strings.
    if n <= 0:
        n = 1

    # Deterministically construct a and b of length n.
    # a uses a simple repeating pattern of '+' and '-'
    # b uses a pattern of '+', '-', '?' so that f can be non-zero.
    pattern_a = ['+', '-']
    pattern_b = ['+', '-', '?']

    a_chars = [pattern_a[i % len(pattern_a)] for i in range(n)]
    b_chars = [pattern_b[i % len(pattern_b)] for i in range(n)]

    a = ''.join(a_chars)
    b = ''.join(b_chars)

    result = compute_probability(a, b)
    print(result)

if __name__ == "__main__":
    main(10)