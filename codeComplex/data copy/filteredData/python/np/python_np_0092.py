import math

def C(a, b):
    return math.factorial(a) // (math.factorial(b) * math.factorial(a - b))

def solve(a, b):
    x, y, d, ans, power = 0, 0, 0, 0, 0
    for i in range(len(a)):
        if a[i] == '+':
            x += 1
        if a[i] == '-':
            x -= 1
        if b[i] == '?':
            d += 1
        if b[i] == '+':
            y += 1
        if b[i] == '-':
            y -= 1
    plus, minus = d, 0
    for _ in range(0, d + 1):
        k = C(d, plus)
        if y + (plus - minus) == x:
            ans += k
        power += k
        plus -= 1
        minus += 1
    return "{0:.12f}".format(ans / power)

def generate_input(n):
    if n < 1:
        n = 1
    # length of strings
    length = n
    # a: first n//2 are '+', rest are '-'
    a = ['+' if i < length // 2 else '-' for i in range(length)]
    # b: pattern '+-?' repeated
    pattern = ['+', '-', '?']
    b = [pattern[i % 3] for i in range(length)]
    return a, b

def main(n):
    a, b = generate_input(n)
    result = solve(a, b)
    print(result)

if __name__ == "__main__":
    main(10)