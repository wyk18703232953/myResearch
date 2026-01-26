def main(n):
    l = n // 2
    r = n
    if l > r:
        l, r = r, l

    ans = l ^ r
    j = 0
    while (1 << j) <= ans:
        ans |= (1 << j)
        j += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)