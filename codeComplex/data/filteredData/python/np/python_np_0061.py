from collections import Counter
import math

def main(n):
    # Generate two deterministic strings consisting of '+' and '-' with size based on n
    # First string length: n
    # Second string length: n//2
    s_len = n
    t_len = max(1, n // 2)

    s = [('+' if i % 2 == 0 else '-') for i in range(s_len)]
    t = [('+' if i % 3 == 0 else '-') for i in range(t_len)]

    a = Counter(s)
    b = Counter(t)
    if a['+'] < b['+'] or a['-'] < b['-']:
        print("0")
        return
    else:
        a1 = a['+'] - b['+']
        b1 = a['-'] - b['-']
    s_val = math.factorial(a1 + b1) // (math.factorial(a1) * math.factorial(b1))
    s1 = float(2 ** (a1 + b1))
    print(s_val / s1)

if __name__ == "__main__":
    main(1000)