def main(n):
    m = 1 << (n - 1) if n > 1 else 1
    v = [0] * 51
    left = 1
    right = n
    for i in range(1, n + 1):
        if n - i - 1 <= 0:
            pw = 1
        else:
            pw = 1 << (n - i - 1)
        if m <= pw:
            v[left] = i
            left += 1
        else:
            v[right] = i
            right -= 1
            m -= pw
    for i in range(1, n):
        print(v[i], end=' ')
    print(v[n])


if __name__ == "__main__":
    main(5)