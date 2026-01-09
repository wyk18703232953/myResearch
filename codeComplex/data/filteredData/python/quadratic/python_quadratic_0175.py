def main(n):
    # Map n to problem parameters deterministically
    # Limit k to a reasonable value to keep behavior similar to original constraints
    k = max(1, min(20, n // 2 if n > 1 else 1))
    # Generate array a of length n with values in [0, 255]
    a = [i % 256 for i in range(n)]

    p = [-1] * 256
    p[0] = 0

    for x in a:
        if p[x] < 0:
            for y in range(x - 1, max(-1, x - k), -1):
                if p[y] >= 0:
                    if p[y] + k > x:
                        p[x] = p[y]

                    else:
                        p[x] = p[y + 1] = y + 1
                    break
            if p[x] < 0:
                p[x] = p[x - k + 1] = x - k + 1

    b = [p[x] for x in a]
    # print(' '.join(map(str, b)))
    pass
if __name__ == "__main__":
    main(10)