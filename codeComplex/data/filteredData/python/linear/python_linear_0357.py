def main(n):
    s = ''.join(str((i * 7 + 3) % 10) for i in range(n))
    ans = 0
    r, c = 0, 0
    for ch in s:
        r += int(ch)
        c += 1
        if int(ch) % 3 == 0 or r % 3 == 0 or c == 3:
            ans += 1
            r, c = 0, 0
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)