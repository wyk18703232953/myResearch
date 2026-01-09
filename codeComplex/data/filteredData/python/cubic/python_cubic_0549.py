def main(n):
    # Generate deterministic input based on n
    # a: list of digits as characters, length = n, digits cycle 0-9
    # b: upper bound integer with n digits, pattern 9876543210...
    a = [str(i % 10) for i in range(n)]
    b_digits = [str((9 - i) % 10) for i in range(n)]
    b_str = "".join(b_digits) if b_digits else "0"
    b = int(b_str)

    a_list = list(a)
    ans = ""
    a_list.sort(reverse=True)
    while len(a_list) > 0:
        for i in range(len(a_list)):
            num = ans + a_list[i] + "".join(sorted(a_list[:i] + a_list[i + 1:]))
            if int(num) <= b:
                ans += a_list[i]
                a_list = a_list[:i] + a_list[i + 1:]
                break

        else:
            break
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    main(5)