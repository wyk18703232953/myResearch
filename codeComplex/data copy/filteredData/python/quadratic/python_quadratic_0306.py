def main(n):
    # Interpret n as the length of the list; keep k as a fixed proportion of n
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministic choice of k based on n (at least 1 and at most n)
    k = max(1, n // 3)
    if k > n:
        k = n

    # Deterministic list generation: l[i] = i % 7 + i // 3
    l = [i % 7 + i // 3 for i in range(n)]

    ans = 0
    for i in range(n):
        avg = 0
        count = 0
        for j in range(i, n):
            count += l[j]
            if j - i + 1 >= k:
                avg = count / (j - i + 1)
            if avg > ans:
                ans = avg
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)