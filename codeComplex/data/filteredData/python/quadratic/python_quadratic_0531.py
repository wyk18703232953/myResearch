def main(n):
    # Determine sequence length; ensure at least 1
    m = max(1, n)

    # Generate a deterministic permutation for a
    # a is a permutation of 1..m
    a = [(i * 3 + 1) % m + 1 for i in range(m)]

    # Generate a deterministic permutation for b
    # b is another permutation of 1..m
    b = [(i * 5 + 2) % m + 1 for i in range(m)]

    a = a[::-1]
    ans = [0] * m
    marked = [True] * (m + 1)

    for i in range(m):
        if marked[b[i]]:
            while True:
                marked[a[-1]] = False
                ans[i] += 1
                if a[-1] == b[i]:
                    a.pop()
                    break
                a.pop()
        else:
            continue
    print(*ans)


if __name__ == "__main__":
    main(10)