def main(n):
    # Deterministically generate a and b from n
    # a is a number whose digits are 0..9 repeated to reach length n+1 (avoid leading zero)
    # b is a descending number using digits 9..0 repeated to reach same length
    length = max(1, n + 1)

    # generate digits for a (avoid leading zero)
    digits_a = [((i % 9) + 1) for i in range(length)]
    a = 0
    for d in digits_a:
        a = a * 10 + d

    # generate digits for b (allow 0 inside, but first digit non-zero)
    digits_b = []
    for i in range(length):
        if i == 0:
            digits_b.append(9)

        else:
            digits_b.append(9 - (i % 10))
    b = 0
    for d in digits_b:
        b = b * 10 + d

    x = [0] * 10
    temp_a = a
    while temp_a:
        x[temp_a % 10] += 1
        temp_a = temp_a // 10

    ans = 0
    for i in range(9, -1, -1):
        for _ in range(x[i]):
            ans = ans * 10 + i

    if ans <= b:
        # print(ans)
        pass

    else:
        ans = 0
        b_str = str(b)
        for ch in b_str:
            c = int(ch)
            while c >= 0 and not x[c]:
                c -= 1
            if c < 0:
                while True:
                    x[ans % 10] += 1
                    d = ans % 10
                    ans = ans // 10
                    flag = 0
                    for bb in range(d - 1, -1, -1):
                        if x[bb]:
                            ans = ans * 10 + bb
                            x[bb] -= 1
                            flag = 1
                            break
                    if flag:
                        break
                break

            else:
                x[c] -= 1
                ans = ans * 10 + c
                if c < int(ch):
                    break

        for j in range(9, -1, -1):
            for _ in range(x[j]):
                ans = ans * 10 + j
        # print(ans)
        pass
if __name__ == "__main__":
    main(10)