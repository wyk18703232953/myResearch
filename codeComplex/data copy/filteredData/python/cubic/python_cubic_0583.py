def main(n):
    # Generate a deterministic string 'a' and integer 'b' based on n
    # Let the original input be:
    #   first line: a string of digits
    #   second line: an integer b
    #
    # We map n to:
    #   - length of digit string = n
    #   - b is an integer with n digits, constructed deterministically
    #
    # Construct digit string: repeat "0123456789" and take first n digits
    digit_source = "0123456789"
    a_str = "".join(digit_source[i % 10] for i in range(n)) if n > 0 else "0"
    # Construct b: a deterministic integer, for example the integer represented
    # by the reversed digits of a_str (ensure no leading zeros issue by fallback)
    b_str = a_str[::-1]
    # Avoid leading zero making integer too small; if leading zero, replace with '1'
    if b_str and b_str[0] == "0":
        b_str = "1" + b_str[1:] if len(b_str) > 1 else "1"
    b = int(b_str)

    # Core algorithm from original program
    a = sorted(a_str)
    a = a[::-1]
    p = ""
    while a:
        for i, z in enumerate(a):
            n_candidate = p + a[i] + "".join(sorted(a[:i] + a[i + 1 :]))
            if int(n_candidate) <= b:
                p += z
                a.pop(i)
                break

    # print(p)
    pass
    return p


if __name__ == "__main__":
    # Example deterministic call for scaling experiments
    main(10)