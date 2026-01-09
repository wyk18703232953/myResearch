def main(n):
    # Generate deterministic data based on n
    # First line total sum t
    t_line = [i % 5 + 1 for i in range(n)]
    t = sum(t_line)

    r = 1
    # Generate n-1 more lines and compare their sums with t
    for i in range(1, n):
        line = [((i + j) % 7) + 1 for j in range(n)]
        if sum(line) > t:
            r += 1

    # print(r)
    pass
if __name__ == "__main__":
    main(10)