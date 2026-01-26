def main(n):
    # Deterministic generation of a and b based on n
    # a: string of digits length n (cycling 0-9)
    # b: string of digits length n+1 (reverse cycling 9-0)
    if n <= 0:
        a_str = "0"
        b_str = "0"

    else:
        a_digits = [str(i % 10) for i in range(n)]
        b_digits = [str((9 - i) % 10) for i in range(n + 1)]
        a_str = "".join(a_digits)
        b_str = "".join(b_digits)

    a = list(a_str)
    b = list(b_str)

    if len(a) < len(b) or len(a) == 1:
        # print(''.join(sorted(a)[::-1]))
        pass

    else:
        ans, tem = 0, []

        for i in range(len(b)):
            for j in range(int(b[i]) - 1, -1, -1):
                if str(j) in a and not (j == i == 0):
                    a.remove(str(j))
                    ans = max(ans, int(''.join(tem) + str(j) + ''.join(sorted(a)[::-1])))
                    a.append(str(j))
                    break

            if b[i] not in a:
                break

            tem.append(b[i])
            a.remove(b[i])

        if tem:
            ans = max(ans, int(''.join(tem)))

        # print(ans)
        pass
if __name__ == "__main__":
    main(10)