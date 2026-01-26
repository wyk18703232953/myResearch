
def d(n):
    ret = 0
    n = list(str(n))
    for i in range(len(n)):
        ret += int(n[i])
    return ret

def main():
    n, s = map(int, input().split())

    l, h = 0, n
    for i in range(2000):
        m = (l + h) // 2
        if m - d(m) >= s:
            h = m
        else:
            l = m

    for i in range(-100, 100):
        t = m + i
        if t < 0 or t > n:
            continue
        if abs(t - d(t)) >= s:
            print(n - t + 1)
            exit()
    print(0)


if __name__ == '__main__':
    main()
