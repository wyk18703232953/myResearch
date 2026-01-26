import math

def generate_strings(n):
    length = max(1, n)
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(length))
    t = ''.join('+' if i % 3 == 0 else ('-' if i % 3 == 1 else '?') for i in range(length))
    return s, t

def compute_probability(s, t):
    p1, p2, m1, m2, q = 0, 0, 0, 0, 0
    for i in s:
        if i == '+':
            p1 += 1
        else:
            m1 += 1
    for i in t:
        if i == '+':
            p2 += 1
        elif i == '-':
            m2 += 1
        else:
            q += 1
    dp, dm = p1 - p2, m1 - m2
    if dp < 0 or dm < 0:
        return 0.0
    ans = (math.factorial(q) / (math.factorial(dp) * math.factorial(dm))) / math.pow(2, q)
    return ans

def main(n):
    s, t = generate_strings(n)
    ans = compute_probability(s, t)
    print(ans)

if __name__ == "__main__":
    main(10)