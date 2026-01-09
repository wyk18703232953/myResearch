def main(n):
    # Interpret n as both length of array and target distinct count m
    m = n
    # Deterministic array generation: repeating pattern to ensure some duplicates
    arr = [(i * 2) % (n // 2 + 1 if n > 1 else 1) for i in range(1, n + 1)]

    d = {}
    i = 1
    for x in arr:
        if len(d) == m:
            break
        d[x] = i
        i += 1
    if len(d) == m:
        # print(min(d.values()), max(d.values()))
        pass

    else:
        # print(-1, -1)
        pass
if __name__ == "__main__":
    main(10)