def main(n):
    # Generate deterministic data: n integers with some repetitions
    # Example pattern: a_i = (i % (n // 3 + 1)) + 1 to ensure many duplicates and divisibility relations
    if n <= 0:
        # print(0)
        pass
        return

    arr = [(i % (n // 3 + 1)) + 1 for i in range(n)]

    a = sorted(list(set(arr)))
    m = len(a)
    used = [0] * m
    cnt = 0
    for i in range(m):
        if not used[i]:
            used[i] = 1
            cnt += 1
            for j in range(i + 1, m):
                if a[j] % a[i] == 0:
                    used[j] = 1
    # print(cnt)
    pass
if __name__ == "__main__":
    main(1000)