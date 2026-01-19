import math

def compute_probability(a, b):
    c = 0
    d = 0
    q = 0
    for ch in a:
        if ch == "+":
            c += 1
        elif ch == "-":
            c -= 1
    for ch in b:
        if ch == "+":
            d += 1
        elif ch == "-":
            d -= 1
        else:
            q += 1
    if c == d:
        return (math.factorial(q) / (math.factorial(q / 2) * math.factorial(q / 2))) / (2 ** q)
    else:
        mx = d + q
        mn = d - q
        if c > mx or c < mn:
            return 0.0
        else:
            ans = c - d
            if ans > 0:
                return (math.factorial(q) / (math.factorial(((q - ans) / 2) + ans) * math.factorial((q - ans) / 2))) / (2 ** q)
            else:
                return (math.factorial(q) / (math.factorial((q - ans) / 2) * math.factorial(((q - ans) / 2) + ans))) / (2 ** q)

def generate_strings(n):
    # deterministic generation of a and b based on n
    # length of a and b is n
    # a[i]: '+' if i % 2 == 0 else '-'
    # b[i]: '+' if i % 3 == 0, '-' if i % 3 == 1, '?' if i % 3 == 2
    a = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    b_chars = []
    for i in range(n):
        r = i % 3
        if r == 0:
            b_chars.append('+')
        elif r == 1:
            b_chars.append('-')
        else:
            b_chars.append('?')
    b = ''.join(b_chars)
    return a, b

def main(n):
    a, b = generate_strings(n)
    result = compute_probability(a, b)
    print(result)

if __name__ == "__main__":
    main(10)