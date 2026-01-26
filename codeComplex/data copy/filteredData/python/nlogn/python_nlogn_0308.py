def main(n):
    # Generate deterministic data based on n
    # Simulate original input structure:
    # First line: n
    # Second line: n integers
    # Third line: a string of '0' and '1' of length n

    # Generate the list of integers (second line)
    # Use a simple deterministic pattern: a[i] = (i * 3) % n
    # To avoid all zeros when n=1, handle small n separately
    if n <= 0:
        return

    arr = [(i * 3) % n for i in range(1, n + 1)]

    # Generate the command string (third line)
    # Pattern: first min(k, n) zeros then remaining ones,
    # where k = n // 2 for some balance
    k = n // 2
    cmd_chars = []
    for i in range(n):
        if i < k:
            cmd_chars.append('0')

        else:
            cmd_chars.append('1')
    cmd = ''.join(cmd_chars)

    # Core logic from original program
    i_iter = iter(sorted(zip(arr, range(1, n + 1))))
    s, o = [], []
    for c in cmd:
        if c == '0':
            x = next(i_iter)[1]
            o.append(x)
            s.append(x)

        else:
            o.append(s.pop())

    # print(*o)
    pass
if __name__ == "__main__":
    main(10)