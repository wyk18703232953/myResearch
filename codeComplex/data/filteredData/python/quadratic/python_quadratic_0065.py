def main(n):
    # n: length of nums and also number of queries m
    if n <= 0:
        return

    # Deterministic generation of nums based on n
    # Example: a simple pattern that depends only on n
    nums = [(i * 2 + (n % 3)) % (n + 1) for i in range(n)]

    counts = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                counts += 1

    ans = counts % 2
    ans_tmp = []

    # Deterministic generation of m and (l, r) queries based on n
    m = n
    for i in range(m):
        l = i % n
        r = (n - 1 - i) % n
        if l > r:
            l, r = r, l
        tmp = r - l + 1
        tmp_count = (tmp * (tmp - 1) // 2)
        if tmp_count % 2 == 1:
            ans = (ans + 1) % 2
        ans_tmp.append(ans)

    for i in range(m):
        ans = ans_tmp[i]
        if ans % 2 == 1:
            print("odd")
        else:
            print("even")


if __name__ == "__main__":
    main(10)