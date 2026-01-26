import math

def compute_probability(a: str, b: str) -> float:
    posa = a.count('+') - a.count('-')
    posb = b.count('+') - b.count('-')
    q = b.count('?')
    dist = posa - posb
    ones = (abs(dist) + q) / 2
    if q < abs(dist) or ((dist + q) % 2):
        ans = 0.0
    else:
        ans = float(math.factorial(q) / (math.factorial(ones) * math.factorial(q - ones)))
        ans /= pow(2, q)
    return ans

def main(n: int):
    if n < 1:
        n = 1
    # Original problem structure: two strings a, b of equal length
    # Here we map n to the common length of a and b
    length = n

    # Deterministic construction of a and b
    # a uses a fixed repeating pattern of '+' and '-'
    pattern_a = ['+', '-']
    a = ''.join(pattern_a[i % 2] for i in range(length))

    # b uses '+', '-', '?' in a deterministic pattern based on index
    chars_b = ['+', '-', '?']
    b = ''.join(chars_b[i % 3] for i in range(length))

    ans = compute_probability(a, b)
    print(f'{ans:.9f}')

if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)