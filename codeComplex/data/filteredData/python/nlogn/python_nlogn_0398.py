def main(n):
    v = []
    a = list(range(n))
    for i in range(n):
        x = i % 1000 - 500
        y = (i * 2) % 1000 - 500
        v.append([x, y, x * x + y * y])

    # Deterministic shuffle using a simple linear congruential generator (LCG)
    # No use of random module
    def lcg_shuffle(arr, seed):
        m = 2 ** 31 - 1
        a_lcg = 1103515245
        c_lcg = 12345
        state = seed
        length = len(arr)
        for i in range(length - 1, 0, -1):
            state = (a_lcg * state + c_lcg) % m
            j = state % (i + 1)
            arr[i], arr[j] = arr[j], arr[i]

    iteration = 0
    while True:
        x = 0
        y = 0
        ans = [0] * n
        lcg_shuffle(a, seed=n + iteration)
        for i in range(n):
            xi = v[a[i]][0]
            yi = v[a[i]][1]
            if (x + xi) ** 2 + (y + yi) ** 2 <= (x - xi) ** 2 + (y - yi) ** 2:
                x += xi
                y += yi
                ans[a[i]] = 1
            else:
                x -= xi
                y -= yi
                ans[a[i]] = -1
        if x * x + y * y <= 1500000 ** 2:
            print(*ans)
            break
        iteration += 1


if __name__ == "__main__":
    main(1000)