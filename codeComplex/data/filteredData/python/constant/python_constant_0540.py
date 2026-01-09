def main(n):
    s = n * n + n // 2
    ans = s // n
    s %= n
    if s != 0:
        ans += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)