def main(n):
    # Generate deterministic inputs based on n
    # a is fixed to 26 (length of alphabet)
    a = 26
    # b is derived from n but capped at 26
    b = n if n <= 26 else (n % 26 if n % 26 != 0 else 26)
    # c is first k letters of alphabet, where k depends on n
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    k = (n % 26) if (n % 26) != 0 else 26
    c = alphabet[:k]

    su = 0
    cnt = 0
    j = -2
    i = 0
    lis = "abcdefghijklmnopqrstuvwxyz"
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