def search(current, digits, target, idx, bulk):
    if len(current) == len(target) and int(current) <= int(target):
        print(current)
        exit(0)

    possibilities = [char for char in digits if bulk or (char <= target[idx] and char in digits)]

    if len(possibilities) == 0:
        return None

    for possible_digit in sorted(set(possibilities), reverse=True):
        tmp_digits = list(digits)
        tmp_digits.remove(possible_digit)
        if not bulk:
            bulk = True if possible_digit != target[idx] else False
        search(current + possible_digit, tmp_digits, target, idx + 1, bulk)


def main():
    digits = sorted(list(input()), reverse=True)
    target = input()

    if len(digits) < len(target):
        print(''.join(digits))
        exit(0)

    entries = [char for char in digits if char <= target[0]]

    for current in sorted(set(entries), reverse=True):
        tmp_digits = list(digits)
        tmp_digits.remove(current)
        search(current, tmp_digits, target, 1, True if current != target[0] else False)


if __name__ == "__main__":
    main()
