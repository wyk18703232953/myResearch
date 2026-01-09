def main(n):
    # n controls the length of string c and the value of b (number of characters to pick)
    # Generate c deterministically: first n letters cycling in the alphabet
    lis = "abcdefghijklmnopqrstuvwxyz"
    c = "".join(lis[i % 26] for i in range(n))
    # Set b as n//2 but at least 1
    b = max(1, n // 2)

    su = 0
    cnt = 0
    j = -2
    i = 0
    while i < 26 and cnt < b:
        if lis[i] in c and i - 2 >= j:
            su += i + 1
            cnt += 1
            j = i
        i += 1
    if cnt < b:
        # print(-1)
        pass

    else:
        # print(su)
        pass
if __name__ == "__main__":
    main(10)