def main(n):
    # Interpret n as number of tasks
    # Deterministic parameter generation based on n
    l = n
    r = n * (n + 1) // 2
    x = max(1, n // 3)
    tasks = [i + 1 for i in range(n)]

    cnt = 0
    for num in range(1 << n):
        bin_num = bin(num)[2:]
        if len(bin_num) < n:
            bin_num = '0' * (n - len(bin_num)) + bin_num
        m = []
        for i in range(n):
            if bin_num[i] == '1':
                m.append(tasks[i])
        if m:
            s = sum(m)
            if l <= s <= r and max(m) - min(m) >= x:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main(10)