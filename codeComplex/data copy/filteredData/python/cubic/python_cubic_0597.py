def main(n):
    # Deterministically generate strings a and b based on n
    # Let a be a string of digits of length n
    # Let b be a string of digits of length n (or longer, to exercise both branches)
    # Here: a = "0..9" pattern repeated, b = "9..0" pattern repeated, both length n
    a = "".join(str(i % 10) for i in range(n))
    b = "".join(str(9 - (i % 10)) for i in range(n))

    digits = {}

    def greedy(digits_dict, s):
        for i in range(9, -1, -1):
            d = str(i)
            if d in digits_dict:
                while digits_dict[d] > 0:
                    s += d
                    digits_dict[d] -= 1
        return s

    for d in a:
        if d in digits:
            digits[d] += 1

        else:
            digits[d] = 1

    if len(a) < len(b):
        result = greedy(digits, "")
        # print(result)
        pass

    else:
        ind = 0
        cur = ""
        back = False
        done = False
        output_printed = False

        while True:
            if ind == len(a) or done is True:
                break
            found = False
            for i in range(9, -1, -1):
                x = str(i)
                if i == int(b[ind]) and x in digits and digits[x] > 0:
                    found = True
                    digits[x] -= 1
                    cur += x
                    break
                elif i < int(b[ind]) and x in digits and digits[x] > 0:
                    found = True
                    done = True
                    digits[x] -= 1
                    cur += x
                    result = greedy(digits, cur)
                    # print(result)
                    pass
                    output_printed = True
                    break
            if found is False:
                back = True
                break
            ind += 1

        if back is False and done is False:
            # print(cur)
            pass
        elif done is False:
            for i in range(ind - 1, -1, -1):
                digits[cur[i]] += 1
                for j in range(9, -1, -1):
                    d = str(j)
                    if j < int(b[i]) and d in digits and digits[d] > 0:
                        done = True
                        s = cur[:i]
                        s += d
                        digits[d] -= 1
                        result = greedy(digits, s)
                        # print(result)
                        pass
                        output_printed = True
                        break
                if done:
                    break
        # In extremely degenerate paths there might be no print at all in original logic.
        # For determinism of experiments, ensure at least some output.
        if not output_printed and len(cur) > 0:
            # print(cur)
            pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)