n = None
k = None
s = None

def generate_input(n):
    k = n if n > 0 else 1
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n if n > 0 else 1))
    return n if n > 0 else 1, k, s

def main(n_input):
    n, k, s = generate_input(n_input)
    f = 0
    for i in range(1, n):
        if s[:n - i] == s[i:]:
            f = 1
            break
    if f == 0:
        print(s * k)
    else:
        j = n - i
        final = s[j:]
        print(s + final * (k - 1))

if __name__ == "__main__":
    main(5)