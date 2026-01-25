def main(n):
    # n: length of the digit string a
    # generate a deterministic digit string of length n
    if n <= 0:
        a = ""
    else:
        # cycle digits 1..9 then 0 to avoid all-zero except when n == 0
        digits = "1234567890"
        a = "".join(digits[i % 10] for i in range(n))

    total = 0
    for x in a:
        total += int(x)

    ans = "NO"
    if total == 0:
        ans = "YES"

    s = 1
    while s * s <= total and ans == "NO":
        if total % s == 0:
            t = 0
            flag = 0
            for x in a:
                t += int(x)
                if t == s:
                    flag = 1
                if t > s:
                    if flag == 1:
                        flag = 0
                        t = int(x)
                        if t == s:
                            flag = 1
            if t == s and t != total:
                ans = "YES"

            t = 0
            flag = 0
            block = total // s
            for x in a:
                t += int(x)
                if t == block:
                    flag = 1
                if t > block:
                    if flag == 1:
                        flag = 0
                        t = int(x)
                        if t == block:
                            flag = 1
            if t == block and t != total:
                ans = "YES"
        s += 1

    print(ans)


if __name__ == "__main__":
    main(10)