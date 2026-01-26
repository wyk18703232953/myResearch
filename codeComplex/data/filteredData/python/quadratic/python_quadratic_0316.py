def main(n):
    # Interpret n as length of array, k as n // 2 (at least 1)
    if n <= 0:
        # print(0.0)
        pass
        return

    k = max(1, n // 2)

    # Deterministic array generation: arr[i] = (i * 3 + 1) % 1000
    arr = [(i * 3 + 1) % 1000 for i in range(n)]

    avg = 0.0
    for i in range(n):
        cnt = 0
        s = 0
        for j in range(i, n):
            s += arr[j]
            cnt += 1
            if cnt >= k:
                current = s / cnt
                if current > avg:
                    avg = current
    # print(avg)
    pass
if __name__ == "__main__":
    main(10)