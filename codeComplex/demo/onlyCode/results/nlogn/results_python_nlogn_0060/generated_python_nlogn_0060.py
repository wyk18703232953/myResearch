def main(n):
    s = ' '.join(str(i % 10) for i in range(1, n + 1))
    a = list(map(int, s.split()))
    k = sorted(a)
    b = 0
    q = 0
    m = 0
    for i in k:
        b = b + i
    for i in k[::-1]:
        q = q + i
        m = m + 1
        if q > (b / 2):
            break
    return m

if __name__ == "__main__":
    print(main(10))