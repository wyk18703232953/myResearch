def main(n):
    # Generate two non-negative integers a and b as strings, based on n
    # Ensure they are different to exercise the else-branch
    a_int = n
    b_int = n + 1
    a = str(a_int)
    b = str(b_int)

    if a == b:
        # print("0")
        pass

    else:
        xor_str = bin(int(a) ^ int(b))[2:]
        a_bin = bin(int(a))[2:]
        b_bin = bin(int(b))[2:]
        ans = ""
        if a_bin[0] == b_bin[0]:
            ans += "0"

        else:
            ans += "1"
        for _ in range(len(xor_str)):
            ans += "1"
        # print(int(ans, 2))
        pass
if __name__ == "__main__":
    main(10)