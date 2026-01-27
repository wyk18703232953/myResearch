def main(n):
    l = n
    r = 3 * n + 1
    if l % 2:
        l += 1
    if r - l < 2:
        # print(-1)
        pass

    else:
        # print(l, l + 1, l + 2)
        pass
if __name__ == "__main__":
    main(10)