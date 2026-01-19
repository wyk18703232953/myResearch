import math

def solve(a, b):
    x1 = a.count('+')
    y1 = a.count('-')
    x2 = b.count('+')
    y2 = b.count('-')
    l = b.count('?')
    if l == 0 and (x1 == x2 and y1 == y2):
        return float(1)
    elif x1 > (x2 + l) or y1 > (y2 + l):
        return float(0)
    else:
        w = math.factorial(l)
        m = math.factorial(x1 - x2)
        n = math.factorial(l - (x1 - x2))
        return (w / (m * n)) / 2 ** (x1 + y1 - x2 - y2)

def main(n):
    # n controls the length of the strings
    length = max(1, n)
    # construct a deterministic target string a of '+' and '-'
    a = ''.join('+' if i % 2 == 0 else '-' for i in range(length))
    # construct b with some '?' positions deterministically
    # pattern: cycle through '+', '-', '?'
    pattern = ['+', '-', '?']
    b = ''.join(pattern[i % 3] for i in range(length))
    result = solve(a, b)
    print(result)

if __name__ == "__main__":
    main(10)