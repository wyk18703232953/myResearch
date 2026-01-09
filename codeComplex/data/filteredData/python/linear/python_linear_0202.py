def main(n):
    s = n % 60 + 1
    a = []
    base = 0
    for i in range(n):
        total_minutes = (base + i * (s + 2)) % (24 * 60)
        a.append(total_minutes)
    if a[0] != 0 and a[0] > s:
        # print(0, 0)
        pass

    else:
        a.append(a[n - 1] + 2 * s + 3)
        for i in range(1, n + 1):
            if a[i] - (a[i - 1] + 2 + s) >= s:
                x = (a[i - 1] + s + 1) // 60
                y = (a[i - 1] + s + 1) % 60
                # print(x, y)
                pass
                break


if __name__ == "__main__":
    main(10)