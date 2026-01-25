from math import gcd

def generate_input(n):
    # Generate n expressions of the form "(a+b)/c"
    # Use deterministic arithmetic patterns based on n and index i
    lines = []
    for i in range(1, n + 1):
        # Deterministic values depending on i and n
        a = i
        b = i % (n + 1)
        c = (i // 2 + 1)
        # Ensure denominator not zero
        if c == 0:
            c = 1
        s = f"({a}+{b})/{c}"
        lines.append(s)
    return lines

def core_logic(expressions):
    d = dict()
    qs = []
    for s in expressions:
        a = int(s[1:s.index('+')])
        b = int(s[s.index('+') + 1: s.index(')')])
        c = int(s[s.index(')') + 2:])
        a = a + b
        gc = gcd(a, c)
        res = (a // gc, c // gc)
        qs.append(res)
        if res in d:
            d[res] += 1
        else:
            d[res] = 1
    output_parts = []
    for q in qs:
        output_parts.append(str(d[q]))
    return ' '.join(output_parts)

def main(n):
    expressions = generate_input(n)
    result = core_logic(expressions)
    print(result)

if __name__ == "__main__":
    main(10)