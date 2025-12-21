def main(n):
    INF = float('inf')
    xw = []
    for i in range(n):
        x = i * 2
        w = 1
        xw.append([x, w])

    rl = []
    for x, w in xw:
        rl.append((x - w, x + w))

    rl.sort(key=lambda x: (x[1], x[0]))

    ans = 0
    tmp = -INF

    for r, l in rl:
        if r < tmp:
            continue
        ans += 1
        tmp = l

    return ans

if __name__ == "__main__":
    print(main(10))