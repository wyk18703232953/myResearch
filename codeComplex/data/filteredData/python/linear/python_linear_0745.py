def main(n):
    mid = n * 2 - 1
    ans = -mid
    while mid > 0:
        ans += mid * 2
        mid -= 2
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)