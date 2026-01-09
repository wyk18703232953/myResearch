def main(n):
    # Deterministically generate strings a and b based on n
    # Use lowercase letters; ensure both are non-empty for n>=1
    letters = [chr(ord('a') + (i % 26)) for i in range(max(1, n))]
    # a is first n chars
    a = ''.join(letters)
    # b is reversed letters with a small deterministic shift
    shift = (n // 2) % max(1, n)
    b_list = letters[-shift:] + letters[:-shift]
    b = ''.join(b_list[::-1])

    if len(a) < len(b):
        a_sorted = sorted(a)[::-1]
        # print(''.join(a_sorted))
        pass
        return

    def check(res, j, a_list, b_str):
        added = False
        tmp = ""
        for ch in a_list:
            if ch == j and not added:
                added = True

            else:
                tmp += ch
        tmp = res + j + tmp[::-1]
        return tmp <= b_str

    # len(a) == len(b) is not guaranteed in generated data.
    # To keep original core logic for the main branch, we enforce equal length
    # by trimming or padding a to match b.
    if len(a) != len(b):
        if len(a) > len(b):
            a = a[:len(b)]

        else:
            # pad a deterministically with 'z' to reach len(b)
            a = a + 'z' * (len(b) - len(a))

    res = ""
    n_len = len(a)
    a_list = sorted(list(a))[::-1]
    for _ in range(n_len):
        for j in list(a_list):
            if check(res, j, a_list, b):
                res += j
                a_list.remove(j)
                break
    # print(res)
    pass
if __name__ == "__main__":
    main(10)