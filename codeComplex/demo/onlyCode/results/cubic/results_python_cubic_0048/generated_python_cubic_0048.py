def main(n):
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    n = len(s)
    for L in range(n - 1, 0, -1):
        if len({s[i:i + L] for i in range(n - L + 1)}) < n - L + 1:
            return L
    return 0

if __name__ == "__main__":
    print(main(10))