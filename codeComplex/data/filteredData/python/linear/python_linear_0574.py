def main(n):
    k = 2
    a = []
    m = n
    while True:
        t = n // k
        if t <= 1:
            k //= 2
            a.extend([k] * m)
            a[-1] = (n // k) * k
            break
        a.extend([k // 2] * (m - t))
        m = t
        k *= 2
    print(' '.join(map(str, a)))


if __name__ == "__main__":
    main(1000)