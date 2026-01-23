import random

def main(n):
    # generate deterministic v based on n
    v = []
    a = list(range(n))
    for i in range(n):
        x = i - n // 2
        y = (i * 2) - n
        v.append([x, y, x * x + y * y])

    # deterministic shuffle: use fixed seed depending on n and iteration
    seed = n
    while True:
        x = 0
        y = 0
        ans = [0] * n

        rnd = random.Random(seed)
        # Fisher-Yates shuffle using deterministic Random instance
        for i in range(n - 1, 0, -1):
            j = rnd.randint(0, i)
            a[i], a[j] = a[j], a[i]

        for i in range(n):
            vx = v[a[i]][0]
            vy = v[a[i]][1]
            if (x + vx) ** 2 + (y + vy) ** 2 <= (x - vx) ** 2 + (y - vy) ** 2:
                x += vx
                y += vy
                ans[a[i]] = 1
            else:
                x -= vx
                y -= vy
                ans[a[i]] = -1

        if x * x + y * y <= 1500000 ** 2:
            print(*ans)
            break

        seed += 1


if __name__ == "__main__":
    main(5)