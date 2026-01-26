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


def main(n):
    # n 控制数字串长度，最小长度设为 1
    length = max(1, n)
    # 确定性构造：周期性数字 0..9
    digits = ''.join(str(i % 10) for i in range(length))
    if check_ticket(digits):
        # print("yes")
        pass

    else:
        # print("no")
        pass
if __name__ == "__main__":
    main(10)