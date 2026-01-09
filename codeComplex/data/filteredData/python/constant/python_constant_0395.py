def main(n):
    # Generate two deterministic binary strings a and b of length n
    # Using '0' and '1' pattern with simple arithmetic
    a = [str((i // 2) % 2) for i in range(n)]
    b = [str((i // 3) % 2) for i in range(n)]

    ans = 0
    for i in range(n):
        if a[i] == "0":
            ans += 1
            if i - 1 >= 0 and a[i] == b[i] == b[i - 1]:
                a[i] = b[i] = b[i - 1] = "X"
            elif i + 1 < n and b[i] == b[i + 1] == a[i + 1] == a[i]:
                a[i] = b[i] = a[i + 1] = "X"
            elif i + 1 < n and a[i] == b[i] == b[i + 1]:
                a[i] = b[i] = b[i + 1] = "X"
            elif i + 1 < n and a[i] == b[i + 1] == a[i + 1]:
                a[i] = b[i + 1] = a[i + 1] = "X"
            elif i + 1 < n and a[i] == b[i] == a[i + 1]:
                a[i] = b[i] = a[i + 1] = "X"

            else:
                ans -= 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)