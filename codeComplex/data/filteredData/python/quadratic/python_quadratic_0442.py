def main(n):
    # Generate deterministic test data:
    # n = length of the array
    # arr[i] = (i % 7) + 1 to avoid zeros and keep values small
    arr = [(i % 7) + 1 for i in range(n)]

    okk = 0
    s = 0
    for i in range(n - 1):
        s += arr[i]
        cnt = 0
        ok = 1
        sss = 0
        for j in range(i + 1, n):
            cnt += arr[j]
            if cnt == s:
                cnt = 0
                sss += 1
            if cnt > s:
                ok = 0
        if cnt == 0 and sss:
            okk = 1
            break
    # print("YES" if okk else "NO")
    pass
if __name__ == "__main__":
    main(10)