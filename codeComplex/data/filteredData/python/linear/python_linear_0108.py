def main(n):
    # n controls the length of s1 and s2
    if n <= 0:
        return ""
    # Deterministic construction of s1 and s2 using simple arithmetic and range
    letters = [chr(ord('a') + (i % 26)) for i in range(n)]
    digits = [chr(ord('0') + (i % 10)) for i in range(n)]
    s1 = "".join(letters)
    s2 = "".join(digits)
    res = s1[0]
    flag = 0
    for i in range(1, len(s1)):
        if s1[i] >= s2[0]:
            res += s2[0]
            flag = 1
            break

        else:
            res += s1[i]
    if flag == 0:
        res += s2[0]
    # print(res)
    pass
    return res


if __name__ == "__main__":
    main(10)