def main(n):
    s = "".join(str((i % 10)) for i in range(1, n + 1)) if n > 0 else "0"
    ans = 0
    r, c = 0, 0
    for ch in s:
        r += int(ch)
        c += 1
        if int(ch) % 3 == 0 or r % 3 == 0 or c == 3:
            ans += 1
            r, c = 0, 0
    print(ans)


if __name__ == "__main__":
    main(10)