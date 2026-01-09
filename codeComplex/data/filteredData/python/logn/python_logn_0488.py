def main(n):
    counter = n
    max_counter = 9
    digits_per_number = 1
    while max_counter < counter:
        digits_per_number += 1
        max_counter = max_counter + digits_per_number * 9 * 10 ** (digits_per_number - 1)
    max_real_number = int(str(9) * digits_per_number)
    dif = max_counter - counter
    rem = dif % digits_per_number
    real_number = max_real_number - dif // digits_per_number
    # print(str(real_number)[-1 - rem])
    pass
if __name__ == "__main__":
    main(10)