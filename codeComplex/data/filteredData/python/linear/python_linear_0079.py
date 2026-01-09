def main(n):
    # Deterministic input generation based on n
    # Define lengths of a and b
    len_a = max(1, n // 2)
    len_b = max(len_a, n)

    # Generate binary strings a and b deterministically
    a = ''.join('1' if i % 2 == 0 else '0' for i in range(len_a))
    b = ''.join('1' if (i * 3) % 5 < 2 else '0' for i in range(len_b))

    # Core algorithm logic
    count = 0
    al = len(a)
    bl = len(b)
    if bl - al + 1 <= 0:
        # print(0)
        pass
        return
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
    # print(count)
    pass
if __name__ == "__main__":
    main(10)