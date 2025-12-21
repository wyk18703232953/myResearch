def main(n):
    k = n
    base_digit_number = 1
    expo = 0
    while k >= base_digit_number:
        base_digit_number += 9 * (expo + 1) * (10 ** expo)
        expo += 1
    base_digit_number -= 9 * (expo) * (10 ** (expo - 1))
    ans_number = (k - base_digit_number) // expo + 10 ** (expo - 1)
    ans_digit = str(ans_number)[(k - base_digit_number) % expo]
    return ans_digit

if __name__ == "__main__":
    print(main(1000))