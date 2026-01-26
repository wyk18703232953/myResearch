n,k = 5, 3
s = "".join(chr(ord('a') + (i % 26)) for i in range(n))

def main(n):
    k = max(2, n // 2 + 1)
    s = "".join(chr(ord('a') + (i % 26)) for i in range(n))

    i = -1
    for j in range(n - 1):
        if s[:j + 1] == s[n - j - 1:]:
            i = j
    add = s[i + 1:]
    for _ in range(k - 1):
        s += add
    # print(s)
    pass
if __name__ == "__main__":
    main(10)