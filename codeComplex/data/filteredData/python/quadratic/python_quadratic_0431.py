def check_ticket(digits):
    for target in range(900):
        seg_i = 0
        seg_sum = 0
        next_flag = False
        for d in digits:
            int_d = int(d)
            if int_d > target:
                next_flag = True
                break
            elif seg_sum + int_d > target:
                if next_flag:
                    break
                next_flag = True
                continue
            elif int_d == target or seg_sum + int_d == target:
                seg_i += 1
                seg_sum = 0

            else:
                seg_sum += int_d

        if next_flag:
            continue

        if seg_i >= 2 and seg_sum == 0:
            return True

    return False


def generate_digits(n):
    if n <= 0:
        return "0"
    digits = []
    for i in range(n):
        digits.append(str(i % 10))
    return "".join(digits)


def main(n):
    digits = generate_digits(n)
    if check_ticket(digits):
        # print("yes")
        pass

    else:
        # print("no")
        pass
if __name__ == "__main__":
    main(20)