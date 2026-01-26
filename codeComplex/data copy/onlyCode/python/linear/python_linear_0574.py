from sys import stdout
def main():
    n = int(raw_input())
    k = 2
    a = []
    m = n
    while 1:
        t = n / k
        if t <= 1:
            k /= 2
            a.extend([k] * m)
            a[-1] = n / k * k
            break
        a.extend([k / 2] * (m - t))
        m = t
        k *= 2
    stdout.write(' '.join(map(str, a)))
main()
