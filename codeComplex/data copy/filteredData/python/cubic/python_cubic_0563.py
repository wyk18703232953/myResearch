def main(n):
    # Deterministically construct inputs a and b from n
    # Ensure n >= 1
    if n < 1:
        n = 1
    # Let a be a string of digits "0..9" repeated, length = n
    a = ''.join(str(i % 10) for i in range(n))
    # Let b length be max(1, n//2), digits pattern "9..0"
    m = max(1, n // 2)
    b = ''.join(str(9 - (i % 10)) for i in range(m))

    length_of_a = len(a)
    length_of_b = len(b)
    found_digit = False
    chk_finnish = False
    appended_digit_count = 0
    n_count = {}
    num = []
    for i in range(0, 10):
        n_count[i] = 0

    for i in range(0, length_of_a):
        c = int(a[i])
        n_count[c] += 1

    output_chars = []

    if length_of_a < length_of_b:
        num = sorted(a, reverse=True)
        for i in range(0, length_of_a):
            output_chars.append(str(num[i]))

    else:
        for i in range(0, length_of_b):
            digit = int(b[i])
            if n_count[digit] > 0:
                num.append(digit)
                n_count[digit] -= 1
                appended_digit_count += 1

            else:
                j = digit - 1
                while j > -1:
                    if n_count[j] > 0:
                        num.append(j)
                        appended_digit_count += 1
                        n_count[j] -= 1
                        found_digit = True
                        chk_finnish = True
                        break
                    j -= 1

                if found_digit:
                    j = 9
                    while j > -1:
                        if n_count[j] > 0:
                            digit_count = n_count[j]
                            for k in range(0, digit_count):
                                num.append(j)
                                n_count[j] -= 1
                                appended_digit_count += 1
                        j -= 1
                    if chk_finnish:
                        break

                else:
                    found_digit = False
                    while found_digit == False:
                        pop_up = num[appended_digit_count - 1]
                        del num[-1]
                        j = pop_up - 1
                        n_count[pop_up] += 1
                        appended_digit_count -= 1
                        while j > -1:
                            if n_count[j] > 0:
                                num.append(j)
                                appended_digit_count += 1
                                n_count[j] -= 1
                                found_digit = True
                                break
                            j -= 1
                    j = 9
                    while j > -1:
                        if n_count[j] > 0:
                            digit_count = n_count[j]
                            for k in range(0, digit_count):
                                num.append(j)
                                appended_digit_count += 1
                        j -= 1
                    break

        for i in range(0, length_of_b):
            output_chars.append(str(num[i]))

    result = ''.join(output_chars)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example deterministic calls for experimentation
    main(10)
    main(50)
    main(100)