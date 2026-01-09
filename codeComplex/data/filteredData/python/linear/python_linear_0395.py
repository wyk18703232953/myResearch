M = 0x3b800001

def main(n):
    a = [i % M for i in range(1, n + 1)]
    wa = 0
    now = 1
    wa += a[-1]
    for i in range(n - 1)[::-1]:
        wa += (now * (n - i - 1) + now * 2) * a[i]
        wa %= M
        now *= 2
        now %= M
    # print(wa % M)
    pass
if __name__ == "__main__":
    main(10)