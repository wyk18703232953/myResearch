def main(n):
    # Interpret n as the length of the array a
    if n <= 0:
        # print(0)
        pass
        return

    d = max(1, n // 3)
    a = [i * 2 for i in range(1, n + 1)]
    a = sorted(a)

    s = set()
    for i in range(n):
        x = a[i] - d
        left = a[i - 1] if i >= 1 else float('inf')
        if abs(x - left) >= d:
            s.add(x)
        x = a[i] + d
        right = a[i + 1] if i + 1 < n else float('inf')
        if abs(x - right) >= d:
            s.add(x)

    # print(len(s))
    pass
if __name__ == "__main__":
    main(10)