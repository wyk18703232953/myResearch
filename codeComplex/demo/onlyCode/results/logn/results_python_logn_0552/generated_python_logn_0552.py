def main(n):
    k = n
    n_digits = 1
    while k - n_digits * 9 * (10 ** (n_digits - 1)) > 0:
        k -= n_digits * 9 * (10 ** (n_digits - 1))
        n_digits += 1
    n_digits -= 1
    if n_digits == 0:
        return k
    nth_num = (k - 1) // (n_digits + 1) + 1
    num = 10 ** n_digits + nth_num - 1
    pos = (k - 1) % (n_digits + 1)
    return int(str(num)[pos])


if __name__ == "__main__":
    print(main(1000))