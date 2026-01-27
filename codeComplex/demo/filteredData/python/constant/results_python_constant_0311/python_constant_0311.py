from sys import stdout

def fn(p, b):
    turns = b[p] // 14
    a = b.copy()
    sm = 0
    a[p] = 0
    for i in range(1, 15):
        a[(p + i) % 14] += turns
    rem = b[p] % 14
    for i in range(p + 1, p + rem + 1, 1):
        a[(i % 14)] += 1
    for i in range(14):
        if a[i] & 1 == 0:
            sm += a[i]
    return sm

def generate_b(n):
    # Deterministic generation of a list of 14 integers based on n
    # Ensure some zeros and some positive values, all dependent on n
    base = n + 1
    b = []
    for i in range(14):
        val = (base * (i + 3) * (i + 1)) % 30
        # keep some zeros but not all
        if (i + n) % 5 == 0:
            val = 0
        b.append(val)
    return b

def main(n):
    b = generate_b(n)
    ans = 0
    for i in range(14):
        if b[i] != 0:
            ans = max(ans, fn(i, b))
    stdout.write(str(ans) + "\n")

if __name__ == "__main__":
    main(10)