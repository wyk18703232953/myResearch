def main(n):
    # Generate deterministic string a and integer string b based on n
    # a: concatenation of digits in range(n, 2*n) modulo 10, at least length 2
    length_a = max(2, n)
    a_digits = [str((n + i) % 10) for i in range(length_a)]
    a = ''.join(a_digits)
    # b: some deterministic integer related to n
    b = str(n * 3 + 7)

    list_a = list(a)
    list_a.sort()
    max_a = int(''.join(list_a))
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            list_a[i], list_a[j] = list_a[j], list_a[i]
            temp_a = int(''.join(list_a))
            if int(b) < temp_a or temp_a <= max_a:
                list_a[i], list_a[j] = list_a[j], list_a[i]

            else:
                max_a = temp_a
    # print(max_a)
    pass
if __name__ == "__main__":
    # Example call; you can change 10 to other sizes when doing experiments
    main(10)