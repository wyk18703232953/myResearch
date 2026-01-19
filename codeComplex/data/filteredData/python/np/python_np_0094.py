import math

def cm(n, r):
    i = n - r
    C = (math.factorial(n)) / (math.factorial(i) * math.factorial(r))
    return C

def generate_inputs(n):
    # s1 and s2 are strings built deterministically from n
    # s1: first n chars, pattern "+-"
    s1 = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    # s2: first n chars, pattern "+-?" repeated
    pattern = ['+', '-', '?']
    s2 = ''.join(pattern[i % 3] for i in range(n))
    return s1, s2

def main(n):
    s1, s2 = generate_inputs(n)
    d1 = {'+': 0, '-': 0}
    d2 = {'+': 0, '-': 0, '?': 0}
    r = 0
    ans = -1

    for c in s1:
        d1[c] += 1
    for c in s2:
        d2[c] += 1

    np_val = d1['+'] - d2['+']
    nn_val = d1['-'] - d2['-']
    if np_val < 0 or nn_val < 0:
        ans = 0
    else:
        n_q = d2['?']
        r = min(np_val, nn_val)
        ans = cm(n_q, r)
        ans = round(float(ans) / float(math.pow(2, n_q)), 9)
    print(ans)

if __name__ == "__main__":
    main(10)