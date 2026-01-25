def main(n):
    # Generate deterministic binary strings a and b based on n
    # Ensure len(b) >= len(a)
    al = max(1, n)
    bl = max(al, 2 * al)

    a = ''.join('1' if (i * 3) % 5 < 2 else '0' for i in range(al))
    b = ''.join('1' if (i * 7) % 11 < 5 else '0' for i in range(bl))

    count = 0
    s = b[:bl - al + 1].count('1')
    for i in range(al - 1):
        if a[i] == '0':
            count += s
        else:
            count += bl - al + 1 - s
        s += int(b[bl - al + i + 1]) - int(b[i])

    if a[-1] == '0':
        count += s
    else:
        count += bl - al + 1 - s

    print(count)


if __name__ == "__main__":
    main(10)