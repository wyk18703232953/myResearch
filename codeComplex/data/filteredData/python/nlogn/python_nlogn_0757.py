def main(n):
    t = n
    results = []
    for case_id in range(1, t + 1):
        size = case_id + 1
        if size < 3:
            size = 3
        ar = [((case_id * 37 + i * 13) % (size + 5)) + 1 for i in range(size)]
        if size <= 2:
            results.append(0)
            continue
        ar_sorted = sorted(ar, reverse=True)
        ans = 0
        for i in range(1, size - 1):
            if ar_sorted[0] > i and ar_sorted[1] > i:
                ans = i
        results.append(ans)
    for v in results:
        print(v)


if __name__ == "__main__":
    main(5)