import math

def binom(n, m):
    return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))

def generate_strings(n):
    # For given n, generate a pair (correct, received) deterministically.
    # Let length of strings be n.
    # correct: first half '+', second half '-'
    half = n // 2
    correct = '+' * half + '-' * (n - half)

    # received: cyclic pattern "+-?" with length n
    pattern = ['+', '-', '?']
    received = ''.join(pattern[i % 3] for i in range(n))
    return correct, received

def main(n):
    correct, received = generate_strings(n)

    plus_correct = correct.count('+')
    min_correct = correct.count('-')
    pos_correct = plus_correct - min_correct

    plus_received = received.count('+')
    min_received = received.count('-')
    unknown = received.count('?')
    pos_received = plus_received - min_received

    diff = abs(pos_correct - pos_received)
    if (diff + unknown) % 2 != 0 or diff > unknown:
        prob = 0.0
    else:
        m = (diff + unknown) // 2
        prob = 1.0 * binom(unknown, m) / (2 ** unknown)
    print(prob)

if __name__ == "__main__":
    main(10)